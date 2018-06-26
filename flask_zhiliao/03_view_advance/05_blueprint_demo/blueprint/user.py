from flask import Blueprint

user_bp = Blueprint('user', __name__, url_prefix='/user')


# 个人档案url蓝图函数
@user_bp.route('/profile/')
def profile():
    return '个人档案页面'


# 个人设置url蓝图函数
@user_bp.route('/settings/')
def settings():
    return '个人设置页面'
