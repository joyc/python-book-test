from flask import Flask, request

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello world!'


@app.route('/list/')
def article_list():
    return 'article list'


@app.route('/p/<int:article_id>')
def article_id(article_id):
    return '您请求的文章是：%s' % article_id


@app.route('/article/<path:test>/')
def test_article(test):
    return 'test path article : %s' % test


@app.route('/u/<uuid:user_id>/')
def user_detail(user_id):
    return '个人用户中心页面： %s' % user_id


# import uuid
# print(uuid.uuid4())

# /blog/<id>/
# /user/<id>/
@app.route('/<any(blog,user):url_path>/<id>/')
def detail(url_path, id):
    if url_path == 'blog':
        return '博客详情页面：%s' % id
    else:
        return '用户详情页面: %s' %id


# http://127.0.0.1:5000/d/?wd=python&ie=utf-8
@app.route('/d/')
def d():
    wd = request.args.get('wd')
    ie = request.args.get('ie')
    return '通过查询字符串的方式传递的参数是： %s, %s' % (wd, ie)


if __name__ == '__main__':
    app.run(debug=True)
