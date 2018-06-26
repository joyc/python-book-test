from flask import Flask, views, url_for, jsonify, render_template, request
from functools import wraps

app = Flask(__name__)


def login_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        # /login/?username=xx
        username = request.args.get('username')
        if username and username == 'erdan':
            return func(*args, **kwargs)
        else:
            return '请先登陆'
    return wrapper


@app.route('/')
def hello_world():
    return 'Hello World!'


# http://127.0.0.1:5000/settings/?username=erdan
# 装饰器要放在url下面，等同于 app.route('/settings/')(login_required('settings'))
# 放在url上面不起作用 等于 login_required(app.route('/settings/')(settings))
@app.route('/settings/')
@login_required
def settings():
    return 'settings page'


class ProfileView(views.View):
    decorators = [login_required]

    def dispatch_request(self):
        return '个人中心页面'


# /profile/?username=erdan
app.add_url_rule('/profile/', view_func=ProfileView.as_view('profile'))


if __name__ == '__main__':
    app.run(debug=True)
