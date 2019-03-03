import platform
from os import environ
from tempfile import mkdtemp
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from tkinter import messagebox
from tkinter.font import nametofont
from datetime import datetime
from queue import Queue
from . import views as v
from . import models as m
from .mainmenu import get_main_menu_for_os
from .images import ABQ_LOGO_32, ABQ_LOGO_64
from . import network as n


class Application(tk.Tk):
    """Application root window"""
    config_dirs = {
        'Linux': environ.get('$XDG_CONFIG_HOME', '~/.config'),
        'freebsd7': environ.get('$XDG_CONFIG_HOME', '~/.config'),
        'Darwin': '~/Library/Application Support',
        'Windows': '~/AppData/Local'
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.title("ABQ Data Entry Application")
        self.resizable(width=False, height=False)

        self.taskbar_icon = tk.PhotoImage(file=ABQ_LOGO_64)
        self.call('wm', 'iconphoto', self._w, self.taskbar_icon)

        self.logo = tk.PhotoImage(file=ABQ_LOGO_32)
        tk.Label(self, image=self.logo).grid(row=0)

        self.inserted_rows = []
        self.updated_rows = []

        datestring = datetime.today().strftime("%Y-%m-%d")
        default_filename = "abq_data_record_{}.csv".format(datestring)
        self.filename = tk.StringVar(value=default_filename)

        # settings model & settings
        config_dir = self.config_dirs.get(platform.system(), '~')
        self.settings_model = m.SettingsModel(path=config_dir)
        self.load_settings()
        self.set_font()
        self.settings['font size'].trace('w', self.set_font)

        style = ttk.Style()
        theme = self.settings.get('theme').get()
        if theme in style.theme_names():
            style.theme_use(theme)

        # create data model

        self.database_login()
        if not hasattr(self, 'data_model'):
            self.destroy()
            return

        self.callbacks = {
            'file->select': self.on_file_select,
            'file->quit': self.quit,
            'show_recordlist': self.show_recordlist,
            'new_record': self.open_record,
            'on_open_record': self.open_record,
            'on_save': self.on_save,
            'get_seed_sample': self.get_current_seed_sample,
            'get_check_tech': self.get_tech_for_lab_check,
            'update_weather_data': self.update_weather_data,
            'upload_to_corporate_rest': self.upload_to_corporate_rest,
            'upload_to_corporate_ftp': self.upload_to_corporate_ftp,
            'show_growth_chart': self.show_growth_chart,
            'show_yield_chart': self.show_yield_chart
        }

        menu_class = get_main_menu_for_os(platform.system())
        menu = menu_class(self, self.settings, self.callbacks)
        self.config(menu=menu)

        # The data record form
        self.recordform = v.DataRecordForm(
            self, self.data_model.fields, self.settings, self.callbacks)
        self.recordform.grid(row=1, padx=10, sticky='NSEW')
        # The data record list
        self.recordlist = v.RecordList(
            self,
            self.callbacks,
            inserted=self.inserted_rows,
            updated=self.updated_rows
        )
        self.recordlist.grid(row=1, padx=10, sticky='NSEW')
        self.populate_recordlist()

        # status bar
        self.status = tk.StringVar()
        self.statusbar = ttk.Label(self, textvariable=self.status)
        self.statusbar.grid(sticky="we", row=3, padx=10)

        self.records_saved = 0

    def show_recordlist(self):
        """Show the recordform"""
        self.recordlist.tkraise()

    def populate_recordlist(self):
        try:
            rows = self.data_model.get_all_records()
        except Exception as e:
            messagebox.showerror(
                title='Error',
                message='Problem reading file',
                detail=str(e)
            )
        else:
            self.recordlist.populate(rows)

    def open_record(self, rowkey=None):
        """Rowkey must be a tuple of (Date, Time, Lab, Plot)"""
        if rowkey is None:
            record = None
        else:
            try:
                record = self.data_model.get_record(*rowkey)
            except Exception as e:
                messagebox.showerror(
                    title='Error',
                    message='Problem reading file',
                    detail=str(e)
                )
                return
        self.recordform.load_record(rowkey, record)
        self.recordform.tkraise()

    def on_save(self):
        """Handles save button clicks"""

        # Check for errors first
        errors = self.recordform.get_errors()
        if errors:
            message = "Cannot save record"
            detail = "The following fields have errors: \n  * {}".format(
                '\n  * '.join(errors.keys())
            )
            self.status.set(
                "Cannot save, error in fields: {}"
                .format(', '.join(errors.keys()))
            )
            messagebox.showerror(title='Error', message=message, detail=detail)

            return False

        data = self.recordform.get()
        try:
            self.data_model.save_record(data)
        except Exception as e:
            messagebox.showerror(
                title='Error',
                message='Problem saving record',
                detail=str(e)
            )
            self.status.set('Problem saving record')

        else:
            self.records_saved += 1
            self.status.set(
                "{} records saved this session".format(self.records_saved)
            )
            key = (data['Date'], data['Time'], data['Lab'], data['Plot'])
            if self.data_model.last_write == 'update':
                self.updated_rows.append(key)
            else:
                # we just inserted a row
                self.inserted_rows.append(key)
            self.populate_recordlist()
            # Only reset the form when we're appending records
            if self.data_model.last_write == 'insert':
                self.recordform.reset()


    def on_file_select(self):
        """Handle the file->select action from the menu"""

        filename = filedialog.asksaveasfilename(
            title='Select the target file for saving records',
            defaultextension='.csv',
            filetypes=[('CSV', '*.csv *.CSV')]
        )
        if filename:
            self.filename.set(filename)
            self.data_model = m.CSVModel(filename=self.filename.get())
            self.populate_recordlist()
            self.inserted_rows = []
            self.updated_rows = []


    def save_settings(self, *args):
        """Save the current settings to a preferences file"""

        for key, variable in self.settings.items():
            self.settings_model.set(key, variable.get())
        self.settings_model.save()

    def load_settings(self):
        """Load settings into our self.settings dict."""

        vartypes = {
            'bool': tk.BooleanVar,
            'str': tk.StringVar,
            'int': tk.IntVar,
            'float': tk.DoubleVar
        }

        # create our dict of settings variables from the model's settings.
        self.settings = {}
        for key, data in self.settings_model.variables.items():
            vartype = vartypes.get(data['type'], tk.StringVar)
            self.settings[key] = vartype(value=data['value'])

        # put a trace on the variables so they get stored when changed.
        for var in self.settings.values():
            var.trace('w', self.save_settings)

    def set_font(self, *args):
        font_size = self.settings['font size'].get()
        font_names = ('TkDefaultFont', 'TkMenuFont', 'TkTextFont')
        for font_name in font_names:
            tk_font = nametofont(font_name)
            tk_font.config(size=font_size)

    def database_login(self):
        """Try to login to the database and create self.data_model"""
        error = ''
        db_host = self.settings['db_host'].get()
        db_name = self.settings['db_name'].get()
        title = "Login to {} at {}".format(db_name, db_host)
        while True:
            login = v.LoginDialog(self, title, error)
            if not login.result:
                break
            else:
                username, password = login.result
                try:
                    self.data_model = m.SQLModel(
                        db_host, db_name, username, password)
                except m.pg.OperationalError:
                    error = "Login Failed"
                else:
                    break

    def get_current_seed_sample(self, *args):
        if not (
            hasattr(self, 'recordform')
            and self.settings['autofill sheet data'].get()
        ):
            return
        data = self.recordform.get()
        plot = data['Plot']
        lab = data['Lab']

        if plot and lab:
            seed = self.data_model.get_current_seed_sample(lab, plot)
            self.recordform.inputs['Seed sample'].set(seed)
            self.recordform.focus_next_empty()

    def get_tech_for_lab_check(self, *args):
        if not (
            hasattr(self, 'recordform')
            and self.settings['autofill sheet data'].get()
        ):
            return
        data = self.recordform.get()
        date = data['Date']
        time = data['Time']
        lab = data['Lab']

        if all([date, time, lab]):
            check = self.data_model.get_lab_check(date, time, lab)
            tech = check['lab_tech'] if check else ''
            self.recordform.inputs['Technician'].set(tech)
            self.recordform.focus_next_empty()

    def update_weather_data(self):

        try:
            weather_data = n.get_local_weather(
                self.settings['weather_station'].get()
            )
        except Exception as e:
            messagebox.showerror(
                title='Error',
                message='Problem retrieving weather data',
                detail=str(e)
            )
            self.status.set('Problem retrieving weather data')
        else:
            self.data_model.add_weather_data(weather_data)
            self.status.set(
                'Weather data recorded for {}'
                .format(weather_data['observation_time_rfc822'])
            )

    def _create_csv_extract(self):
        tmpfilepath = mkdtemp()
        csvmodel = m.CSVModel(
            filename=self.filename.get(), filepath=tmpfilepath)
        records = self.data_model.get_all_records()
        if not records:
            return None
        for record in records:
            csvmodel.save_record(record)

        return csvmodel.filename


    def upload_to_corporate_rest(self):

        csvfile = self._create_csv_extract()

        if csvfile is None:
            messagebox.showwarning(
                title='No records',
                message='There are no records to upload'
            )
            return

        d = v.LoginDialog(
            self,
            'Login to ABQ Corporate REST API'
        )
        if d.result is not None:
            username, password = d.result
        else:
            return
        self.rest_queue = Queue()
        self.uploader = n.CorporateRestUploaderWithQueue(
            csvfile, self.settings['abq_upload_url'].get(),
            self.settings['abq_auth_url'].get(),
            username, password,
            self.rest_queue
        )
        self.uploader.start()
        self.check_queue(self.rest_queue)


    def upload_to_corporate_ftp(self):

        csvfile = self._create_csv_extract()

        d = v.LoginDialog(
            self,
            'Login to ABQ Corporate FTP'
        )

        if d.result is not None:
            username, password = d.result
            try:
                n.upload_to_corporate_ftp(
                    csvfile,
                    self.settings['abq_ftp_host'].get(),
                    self.settings['abq_ftp_port'].get(),
                    username,
                    password
                )
            except n.ftp.all_errors as e:
                messagebox.showerror('Error connecting to ftp', str(e))
            else:
                messagebox.showinfo(
                    'Success',
                    '{} successfully uploaded to FTP'.format(csvfile)
                )

    def check_queue(self, queue):
        if not queue.empty():
            item = queue.get()
            if item.status == 'done':
                messagebox.showinfo(
                    item.status,
                    message=item.subject,
                    detail=item.body
                )
                self.status.set(item.subject)
                return
            elif item.status == 'error':
                messagebox.showerror(
                    item.status,
                    message=item.subject,
                    detail=item.body
                )
                self.status.set(item.subject)
                return
            else:
                self.status.set(item.body)
        self.after(100, self.check_queue, queue)

    def show_growth_chart(self):

        data = self.data_model.get_growth_by_lab()
        max_x = max([x['day'] for x in data])
        max_y = max([x['avg_height'] for x in data])
        popup = tk.Toplevel()
        chart = v.LineChartView(popup, 600, 300, 'day',
                                'centimeters', max_x, max_y)
        chart.pack(fill='both', expand=1)

        legend = {'A': 'green', 'B': 'blue', 'C': 'cyan',
                  'D': 'yellow', 'E': 'purple'}
        chart.draw_legend(legend)

        for lab, color in legend.items():
            dataxy = [
                (x['day'], x['avg_height'])
                for x in data
                if x['lab_id'] == lab]
            chart.plot_line(dataxy, color)

    def show_yield_chart(self):

        popup = tk.Toplevel()
        chart = v.YieldChartView(popup,
            'Average plot humidity', 'Average Plot temperature',
            'Yield as a product of humidity and temperature')
        chart.pack(fill='both', expand=True)

        data = self.data_model.get_yield_by_plot()
        seed_colors = {'AXM477': 'red', 'AXM478': 'yellow',
            'AXM479': 'green', 'AXM480': 'blue'}

        for seed, color in seed_colors.items():
            seed_data = [
                (x['avg_humidity'], x['avg_temperature'], x['yield'])
                for x in data if x['seed_sample'] == seed]
            chart.draw_scatter(seed_data, color, seed)


def main():
    app = Application()
    app.mainloop()
