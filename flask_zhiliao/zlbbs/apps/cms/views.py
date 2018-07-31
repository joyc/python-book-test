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
from .forms import LoginForm, ResetpwdForm, ResetEmailForm
from .models import CMSUser, CMSPermission
from .decorators import login_required, permission_required
import config
from exts import db, mail
from flask_mail import Message
from utils import restful, zlcache
import string
import random


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


@bp.route('/email_captcha/')
def email_captcha():
    # /email_captcha/?email=xxx@xx.com
    email = request.args.get('email')
    if not email:
        return restful.params_error('请传递邮箱参数')
    # 生成验证码string中的字母加range的数字组成
    source = list(string.ascii_letters)
    source.extend(map(lambda x: str(x), range(0, 10)))
    captcha = "".join(random.sample(source, 6))
    # 给邮箱发送内容
    message = Message('Hython论坛邮箱验证码', recipients=[email], body=f'您的验证码为：{captcha}')
    try:
        mail.send(message)
    except:
        return restful.server_error()
    # 存入memcached中
    zlcache.set(email, captcha)
    return restful.success()


@bp.route('/email/')
def send_email():
    message = Message('邮件发送', recipients=['admin@hython.com'], body='测试')
    mail.send(message)
    return 'success!'


@bp.route('/posts/')
@login_required
@permission_required(CMSPermission.POSTER)
def posts():
    return render_template('cms/cms_posts.html')


@bp.route('/comments/')
@login_required
@permission_required(CMSPermission.COMMENTER)
def comments():
    return render_template('cms/cms_comments.html')


@bp.route('/boards/')
@login_required
@permission_required(CMSPermission.BOARDER)
def boards():
    return render_template('cms/cms_boards.html')


@bp.route('/fusers/')
@login_required
@permission_required(CMSPermission.FRONTUSER)
def fusers():
    return render_template('cms/cms_fusers.html')


@bp.route('/cusers/')
@login_required
@permission_required(CMSPermission.CMSUSER)
def cusers():
    return render_template('cms/cms_cusers.html')


@bp.route('/croles/')
@login_required
@permission_required(CMSPermission.ALL_PERMISSION)
def croles():
    return render_template('cms/cms_croles.html')


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


class ResetEmailView(views.MethodView):
    decorators = [login_required]

    def get(self):
        return render_template('cms/cms_resetemail.html')

    def post(self):
        form = ResetEmailForm(request.form)
        if form.validate():
            email = form.email.data
            g.cms_user.email = email
            db.session.commit()
            return restful.success()
        else:
            return restful.params_error(form.get_error())


bp.add_url_rule('/login/', view_func=LoginView.as_view('login'))
bp.add_url_rule('/resetpwd/', view_func=ResetPwdView.as_view('resetpwd'))
bp.add_url_rule('/resetemail/', view_func=ResetEmailView.as_view('resetemail'))
