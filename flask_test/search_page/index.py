# coding:utf-8

from flask import Flask, request, render_template
from spiderData import search_info
import sys


app = Flask(__name__)


@app.route('/')
def index():
    return render_template('/search.html')
    return render_template('/result.html', name='lisi',)


@app.route('/search')
def search():
    keyword = request.args.get('wd')
    print(keyword)
    result = search_info(keyword)
    return render_template('/result.html', data=result, num=len(result))


@app.route('/user/<name>')
def user(name):
    return '<h1>hello, %s!</h1>' % name


if __name__ == '__main__':
    app.run()
