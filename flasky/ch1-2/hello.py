from flask import Flask
from flask_script import Manager


app = Flask(__name__)
manager = Manager(app)


@app.route('/')
def index():
    return '<h1>Hello World!</h1>'


@app.route('/user/<name>')
def user(name):
    return f'<h1>Hello, {name}!</h1>'


@app.route('/id/<int:id>')
# def get_user(id):
#     user = load_user(id)
#     if not user:
#         abort(404)
#     return f'<h3>Hello, Your id is: {id}.</h3>'
#
def id(id):
    return '<h1>Your id is: %d!</h1>' % id


# python hello.py runserver --host 0.0.0.0
if __name__ == '__main__':
    manager.run()
