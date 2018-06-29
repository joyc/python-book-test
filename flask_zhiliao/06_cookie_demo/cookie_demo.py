from flask import Flask, request, Response
from datetime import datetime, timedelta
from cmsviews import bp


app = Flask(__name__)
app.register_blueprint(bp)
app.config['SERVER_NAME'] = 'test.com:5000'


@app.route('/')
def hello_world():
    resp = Response('cookie测试')
    # expires = datetime(year=2018, month=6, day=30, hour=0, minute=0)
    # 使用expires参数需要使用格林尼治时间，比如相对于东京少9小时
    # 距离现在时间一个月、31天
    # 新版本http协议中expries视为废弃，IE8以下不支持max_age
    # 两个参数都指定时优先取max_age，都不设置时默认时间为到浏览器会话结束
    expires = datetime.now() + timedelta(days=30, hours=16)
    resp.set_cookie('username', 'erdan', expires=expires, domain='.test.com')
    return resp


@app.route('/del/')
def delete_cookie():
    resp = Response('删除cookie测试')
    resp.delete_cookie('username')
    return resp


if __name__ == '__main__':
    app.run(debug=True)
