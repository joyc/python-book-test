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


@app.route('/courses/')
def courses():
    return render_template('courses.html', course_name='Python Course')


if __name__ == '__main__':
    app.run()
