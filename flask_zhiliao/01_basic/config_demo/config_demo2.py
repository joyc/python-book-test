from flask import Flask

app = Flask(__name__)
app.config.from_pyfile('config.py', silent=True)  # 后缀任意 第二个参数可在找不到配置文件时指定是否报错True不报错


@app.route('/')
def hello_world():
    return 'Hello world!'


if __name__ == '__main__':
    app.run()
