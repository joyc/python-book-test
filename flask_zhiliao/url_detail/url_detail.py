from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


# url后面一般加/ 利于SEO
@app.route('/list/')
def list():
    return 'list page'


@app.route('/post/', methods=['POST'])
def post():
    return 'just post method is ok'


# 默认的method只有get
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        return 'success'


if __name__ == '__main__':
    app.run(debug=True, port=8000, host='0.0.0.0')
