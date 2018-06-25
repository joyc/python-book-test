from flask import Flask, url_for

app = Flask(__name__)

# / --> hello_world
# hello_world  --> /


@app.route('/')
def hello_world():
    print('my list的url是 :', url_for('my_list', page=2))
    # return 'Hello World!'   #  /list/1?count=2
    return url_for('my_list', page=1, count=2)


@app.route('/list/<page>')
def my_list(page):
    return 'my list'

# url = url_for('login',next='/')
# 会自动的将/编码，不需要手动去处理。
# url=/login/?next=%2F


@app.route('/post/detail/<id>')
def detail(id):
    return 'detail page'


if __name__ == '__main__':
    app.run(debug=True)
