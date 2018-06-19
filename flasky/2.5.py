from flask import Flask
from flask import request


app = Flask(__name__)

@app.route('/')
def index():
    user_agent = request.headers.get('User-Agent')
    return f'<p>Your browser is {user_agent}</p>'


if __name__ == '__main__':
    app.run(debug=True)
