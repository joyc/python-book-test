from flask import Flask, session
import os
from datetime import timedelta


app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(hours=2)


@app.route('/')
def index():
    session['username'] = 'erdansession'
    # session持久化，默认是False，True为31天期限
    session.permanent = True
    return 'Hello World!'


@app.route('/get_session/')
def get_session():
    username = session.get('username')
    print(username)
    return username or "没有session"


@app.route('/del_session/')
def delete_session():
    # session.pop('username')
    session.clear()  # 全部删除
    return "session删除成功"


@app.route('/expries/')
def expries():
    pass


if __name__ == '__main__':
    app.run(debug=True)
