from flask import Flask, url_for
from werkzeug.routing import BaseConverter


app = Flask(__name__)


# 限定变量的字符格式为手机号的url 自定义需继承BaseConverter
class TelephoneConverter(BaseConverter):
    regex = r'1[87534]\d{9}'


# to_python方法的返回值，将会传递到view函数中作为参数。
# to_url方法的返回值，将会在调用url_for函数的时候生成符合要求的URL形式。
# 用户访问/posts/a+b/
class ListConverter(BaseConverter):
    def to_python(self, value):
        return value.split('+')

    def to_url(self, value):
        return '+'.join(value)


# 需加入到converters列表中才生效
app.url_map.converters['tel'] = TelephoneConverter
app.url_map.converters['list'] = ListConverter


@app.route('/')
def hello_world():
    print('='*20)
    print(url_for('posts', boards=['a', 'b']))
    print('=' * 20)
    return 'Hello World!'


@app.route('/user/<int:user_id>/')
def user_profile(user_id):
    return '输入的user_id是:  %s' % user_id


@app.route('/telephone/<tel:my_tel>/')
def my_tel(my_tel):
    return '输入手机号为： %s' % my_tel


@app.route('/posts/<list:boards>/')
def posts(boards):
    print(boards)
    return '请求的版块名称为：%s' % boards


if __name__ == '__main__':
    app.run(debug=True)
