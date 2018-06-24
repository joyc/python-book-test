#! python3
# -*- coding:utf-8 -*-
from flask import Flask, request, url_for, redirect

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello World!'


@app.route('/login/')
def login():
    return '这是登陆页面'


# http://127.0.0.1:5000/profile/?name=chuang
@app.route('/profile/')
def profile():
    if request.args.get('name'):
        return '这是个人中心页面'
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.run(debug=True)