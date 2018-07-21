from flask import session, g
from .views import bp
import config
from .models import CMSUser


@bp.before_request
def before_request():
    if config.CMS_USER_ID in session:
        user_id = session.get(config.CMS_USER_ID)
        user = CMSUser.query.get(user_id)
        # 绑定登陆用户到g上下文
        if user:
            g.cms_user = user