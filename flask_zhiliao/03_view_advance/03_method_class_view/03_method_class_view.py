from flask import Flask, views, url_for, jsonify, render_template, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    if request.method == 'GET':
        return 'Hello World!'
    else:
        # post时的代码
        pass


class LoginView(views.MethodView):
    def __render(self, error=None):
        return render_template('login.html', error=error)

    def get(self):
        return self.__render()

    def post(self):
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'erdan' and password == '123':
            return '登陆成功'
        else:
            return self.__render(error="用户名或密码错误！")


app.add_url_rule('/login/', view_func=LoginView.as_view('login'))


if __name__ == '__main__':
    app.run(debug=True)
