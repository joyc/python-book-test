#! python3
# -*- coding:utf-8 -*-
from flask import Flask, render_template

app = Flask(__name__)
app.config.update({
    'DEBUG': True,
    'TEMPLATES_AUTO_RELOAD': True
    })


@app.route('/')
def index():
    context = {
        'users': ['dadan', 'erdan', 'sandan'],
        'person': {
            'username': 'zhiliao',
            'age': 20,
            'country': 'china'
        },
        'books': [
            {
                'name': '三国演义',
                'author': '罗贯中',
                'price': 110
            },
            {
                'name': '红楼梦',
                'author': '曹雪芹',
                'price': 150
            },
            {
                'name': '西游记',
                'author': '吴承恩',
                'price': 130
            },
            {
                'name': '水浒传',
                'author': '施耐庵',
                'price': 160
            }
        ]
    }
    return render_template('index.html', **context)


if __name__ == '__main__':
    app.run()