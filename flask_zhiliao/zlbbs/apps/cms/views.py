# encoding: utf-8

from flask import Blueprint, views, render_template, request, session, \
    redirect, url_for
from .forms import LoginForm
from .models import CMSUser
from .decorators import login_required
import config


bp = Blueprint("cms", __name__, url_prefix="/cms")


@bp.route('/')
@login_required
def index():
    return 'cms index'


class LoginView(views.MethodView):

    def get(self, message=None):
        return render_template("cms/cms_login.html", message=message)

    def post(self):
        form = LoginForm(request.form)
        if form.validate():
            email = form.email.data
            password = form.password.data
            remember = form.remember.data
            user = CMSUser.query.filter_by(email=email).first()
            if user and user.check_password(password):
                session[config.CMS_USER_ID] = user.id
                if remember:
                    # 如果设置permanent = True则过期时间为31天或者从config中自定义设置
                    session.permanent = True
                    # 即便是当前蓝图也需要指定
                return redirect(url_for("cms.index"))
            else:
                return self.get(message='邮箱或密码错误')
        else:
            # print(form.errors)
            message = form.errors.popitem()[1][0]
            # {'password': ['请输入正确格式的密码']}
            return self.get(message='表单验证错误')


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
