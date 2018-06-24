from flask import Flask, url_for

app = Flask(__name__)

# / --> hello_world
# hello_world  --> /


@app.route('/')
def hello_world():
    print('my list的url是 :', url_for('my_list', page=2))
    # return 'Hello World!'
    return url_for('my_list', page=1, count=2)


@app.route('/list/<page>')
def my_list(page):
    return 'my list'


if __name__ == '__main__':
    app.run(debug=True)
