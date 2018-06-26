from flask import Blueprint, render_template, url_for

# 蓝图模板文件优先查找项目默认templates文件路径
news_bp = Blueprint('news', __name__, url_prefix='/news', 
    template_folder='news_tmp', static_folder='news_static')


@news_bp.route('/list/')
def news_list():
    print(url_for('news.detail'))
    return render_template('news_list.html')


@news_bp.route('/detail/')
def detail():
    return 'detail page'
