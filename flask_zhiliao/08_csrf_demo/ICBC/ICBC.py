from flask import Flask, render_template, views, request, session
from forms import RegistForm, LoginForm, TransferForm
from exts import db
from models import User
import config
from auth import login_required
from flask_wtf import CSRFProtect


app = Flask(__name__)
app.config.from_object(config)
db.init_app(app)
CSRFProtect(app)


@app.route('/')
def index():
    return render_template("index.html")


class RegistView(views.MethodView):

    def get(self):
        return render_template("regist.html")

    def post(self):
        form = RegistForm(request.form)
        if form.validate():
            email = form.email.data
            username = form.username.data
            password = form.password.data
            deposit = form.deposit.data
            user = User(email=email, username=username,
                        password=password, deposit=deposit)
            db.session.add(user)
            db.session.commit()
            return "注册成功！"
        else:
            print(form.errors)
            return "注册失败！"


class LoginView(views.MethodView):
    def get(self):
        return render_template('login.html')

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            user = User.query.filter(User.email == email,
                                     User.password == password).first()
            if user:
                session['user_id'] = user.id
                return '登陆成功！'
            else:
                print(form.errors)
                return '登录不对，邮箱或密码不正确！'


class TransferView(views.MethodView):

    decorators = [login_required]

    def get(self):
        return render_template("transfer.html")

    def post(self):
        form = TransferForm(request.form)
        if form.validate():
            email = form.email.data
            money = form.money.data
            # 验证用户存在
            user = User.query.filter_by(email=email).first()
            if user:
                user_id = session.get("user_id")
                myself = User.query.get(user_id)
                if myself.deposit >= money:
                    user.deposit += money
                    myself.deposit -= money
                    db.session.commit()
                    return "转账成功！"
                else:
                    return "余额不足！"
            else:
                return "该用户不存在！"
        else:
            return "金额填写不正确！"


app.add_url_rule('/regist/', view_func=RegistView.as_view('regist'))
app.add_url_rule('/login/', view_func=LoginView.as_view('login'))
app.add_url_rule('/transfer/', view_func=TransferView.as_view('transfer'))


if __name__ == '__main__':
    app.run(debug=True)
