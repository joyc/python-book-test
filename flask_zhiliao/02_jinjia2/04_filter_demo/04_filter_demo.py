#! python3
# -*- coding:utf-8 -*-
from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)
app.config['TEMPLATES_AUTO_RELOAD'] = True


@app.route('/')
def index():
    context = {
        'position': -9,
        'signature': None,
        'javascript': '<script>alert("hello!,javascript test!")</script>',
        'escape_content': '<script>alert("hello!,escape test!")</script>',
        'safe_content': '<script>alert("hello!,safe test!")</script>',
        'person': ['laoda', 'erdan', 'asan'],
        'age': 19,
        'article': 'hello! ni hao hello world!',
        'create_time': datetime(2018, 6, 25, 10, 0, 0)
    }
    return render_template('index.html', **context)


# 自定义过滤器的实现 过滤器本质上就是一个函数 需用装饰器定义
@app.template_filter('my_cut')
def cut(value):
    value = value.replace("hello", '')
    return value


@app.template_filter('handle_time')
def handle_time(time):
    """
    time距离现在的时间间隔
    1. 如果时间间隔小于1分钟，显示“刚刚”
    2. 如果间隔大于1分钟小于1小时，显示“xx分钟前”
    3. 如果是大于1小时小于24小时，显示“xx小时前”
    4. 如果大于24小时小于30天，显示“xx天前”
    5. 否则显示具体时间  2018/06/25 11:35
    """
    if isinstance(time, datetime):
        now = datetime.now()
        timestamp = (now - time).total_seconds()
        if timestamp < 60:
            return '刚刚'
        elif timestamp >= 60 and timestamp < 60*60:
            minutes = timestamp / 60
            return "%s分钟前" % int(minutes)
        elif timestamp >= 60*60 and timestamp < 60*60*24:
            hours = timestamp / (60*60)
            return "%s小时前" % int(hours)
        elif timestamp >= 60*60*24 and timestamp < 60*60*24*30:
            days = timestamp / (60*60*24)
            return "%s天前" % int(days)
        else:
            return time.strftime('%Y/%m/%d %H:%M')
    else:
        return time


if __name__ == '__main__':
    app.run(debug=True)
