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
    return render_template('index.html')


if __name__ == '__main__':
    app.run()
