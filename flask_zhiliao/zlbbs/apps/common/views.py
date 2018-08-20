#encoding: utf-8

from flask import Blueprint, request
from exts import alidayu
from utils import restful
from utils.captcha import Captcha


bp = Blueprint("common", __name__, url_prefix="/c")


@bp.route('/sms_captcha/')
def sms_captcha():
    # ?telephone=xxx
    # /c/sms_captcha/xxx
    telephone = request.args.get('telephone')
    if not telephone:
        return restful.params_error(message='请传入手机号码！')

    captcha = Captcha.gene_text(number=4)
    if alidayu.send_sms(telephone, code=captcha):
        return restful.success()
    else:
        return restful.params_error(message='短信验证码发送失败!')
