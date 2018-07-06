# encoding: utf-8

from flask import (
    Blueprint,
    views,
    render_template,
    request, session,
    redirect,
    url_for,
    g,
    jsonify
    )
from .forms import LoginForm, ResetpwdForm
from .models import CMSUser
from .decorators import login_required
import config
from exts import db
from utils import restful


bp = Blueprint("cms", __name__, url_prefix="/cms")


@bp.route('/')
@login_required
def index():
    # g.cms_user 可以使用
    return render_template("cms/cms_index.html")


@bp.route('/logout/')
@login_required
def logout():
    del session[config.CMS_USER_ID]
    return redirect(url_for('cms.login'))


@bp.route('/profile/')
@login_required
def profile():
    return render_template("cms/cms_profile.html")


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
            # message = form.errors.popitem()[1][0] 被下面的替代
            message = form.get_error()
            # {'password': ['请输入正确格式的密码']}
            return self.get(message=message)


class ResetPwdView(views.MethodView):
    # 类中装饰器
    decorators = [login_required]

    def get(self):
        return render_template("cms/cms_resetpwd.html")

    def post(self):
        form = ResetpwdForm(request.form)
        if form.validate():
            oldpwd = form.oldpwd.data
            newpwd = form.newpwd.data
            user = g.cms_user
            if user.check_password(oldpwd):
                user.password = newpwd
                db.session.commit()
                # {"code": 200, "message": ""}
                # return jsonify({"code": 200, "message": ""})
                # return restful.restful_result(200, message="", data=None)
                return restful.success()
            else:
                # return jsonify({"code": 400, "message": "旧密码错误！"})
                return restful.params_error("旧密码错误！")
        else:
            # message = form.get_error()
            # return jsonify({"code": 400, "message": message})
            return restful.params_error(form.get_error())


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
