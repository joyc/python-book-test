from flask import Blueprint


# subdomain参数可以为蓝图实现子域名
cms_bp = Blueprint('cms', __name__, subdomain='cms')


@cms_bp.route('/')
def index():
    return 'cms index page'
