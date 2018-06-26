from flask import Flask, url_for, render_template
from blueprint.user import user_bp
from blueprint.news import news_bp
from blueprint.cms import cms_bp


app = Flask(__name__)
app.config['SERVER_NAME'] = 'test.com:5000'
app.register_blueprint(user_bp)
app.register_blueprint(news_bp)
app.register_blueprint(cms_bp)

# 用户模块
# 新闻模块
# 电影模块
# 读书模块


@app.route('/')
def hello_world():
    # 反转url需要指定蓝图名字
    print(url_for('news.news_list'))
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
