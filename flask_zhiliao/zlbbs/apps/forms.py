from wtforms import Form


class BaseForm(Form):
    def get_error(self):
        # 取第一个错误信息
        message = self.errors.popotem()[1][0]
        return message
