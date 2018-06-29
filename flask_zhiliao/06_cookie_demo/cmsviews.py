from flask import Blueprint, request


bp = Blueprint('cms', __name__, subdomain='cms')


@bp.route('/')
def index():
    # request.args
    # request.form
    # request.files
    username = request.cookies.get('username')
    # return 'CMS 首页'
    return username or "没有获取到cookie信息"
