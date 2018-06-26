from flask import Flask, views, url_for, jsonify, render_template

app = Flask(__name__)


# 类视图使用案例：有几个url需要返回json数据
class JSONView(views.View):
    def get_data(self):
        raise NotImplementedError

    def dispatch_request(self):
        return jsonify(self.get_data())


class ListView(JSONView):
    """doc"""
    def get_data(self):
        return {'username': 'erdan', 'password': 112233}


# 例子2：有几个视图需要返回相同变量
class ADSview(views.View):
    def __init__(self):
        super(ADSview, self).__init__()
        self.context = {
            'username': "erdan",
            'ads': "This is Common ADs"
        }


class LoginView(ADSview):
    def dispatch_request(self):
        return render_template('login.html', **self.context)


class RegistView(ADSview):
    def dispatch_request(self):
        return render_template('regist.html', **self.context)


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))


# 需要继承views.View, 且实现dispach_request
# class ListView(views.View):
#     def dispatch_request(self):
#         return "list view"


# as_view 返回函数dispach_request, endpoint不指定默认用as_view函数名
app.add_url_rule('/list/', endpoint='list', view_func=ListView.as_view('list'))


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run(debug=True)
