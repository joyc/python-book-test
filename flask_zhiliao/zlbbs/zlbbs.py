from flask import Flask

app = Flask(__name__)

# config.py exts.py models.py manage.py
# 蓝图：前台 后台 公共


@app.route('/')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
