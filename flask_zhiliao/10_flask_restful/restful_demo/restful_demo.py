from flask import Flask, render_template, url_for
from flask_restful import Api, Resource, reqparse, inputs


app = Flask(__name__)
api = Api(app)


class LoginView(Resource):
    def post(self):
        # username
        # pasword
        parser = reqparse.RequestParser()
        # parser.add_argument('username', type=str, help='用户名验证错误！', required=True, trim=True)
        # parser.add_argument('password', type=str, help='密码验证错误!')
        # parser.add_argument('age', type=int, help='年龄验证错误！')
        # parser.add_argument('gender', type=str, choices=['male', 'female', 'secret'])
        # parser.add_argument('home_page', type=inputs.url, help="网址验证错误！")
        parser.add_argument('telphone', type=inputs.regex(r'1[3578]\d{9}'))
        parser.add_argument('birthday', type=inputs.date, help="生日验证错误")

        args = parser.parse_args()
        print(args)
        return {'username': 'zhiliao'}


# api.add_resource(LoginView, '/login/<username>', endpoint='login')
api.add_resource(LoginView, '/login/')


# with app.test_request_context():
#     print(url_for("loginview"))


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == '__main__':
    app.run(debug=True)
