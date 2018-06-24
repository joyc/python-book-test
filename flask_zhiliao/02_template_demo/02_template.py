#! python3
# -*- coding:utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    context = {
        'username': 'nishishi',
        'age': 18,
        'country': 'china',
        'children': {
            'name': 'Laoda',
            'heigh': 150
        }
    }
    # return render_template('index.html', username='nishishi', age=19, country='china')
    return render_template('index.html', **context)  # 转换为关键字参数


@app.route('/list/')
def my_list():
    return render_template('posts/list.html')


if __name__ == '__main__':
    app.run(debug=True)