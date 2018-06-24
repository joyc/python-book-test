#! python3
# -*- coding:utf-8 -*-
from flask import Flask, Response, jsonify

app = Flask(__name__)


# 将视图函数中返回的字典，转换成json对象，然后返回
# restful-api
class JSONResponse(Response):

    @classmethod
    def force_type(cls, response, environ=None):
        """
        这个方法只有视图函数返回非字符及元组和非Response对象时才会被调用
        response：视图函数的返回值
        """
        # print(response)
        # print(type(response))
        # return Response('hello')
        if isinstance(response, dict):
            # jsonify除了将字典转换成json对象，还将改对象包装成了一个Response对象
            response = jsonify(response)
        return super(JSONResponse, cls).force_type(response, environ)


app.response_class = JSONResponse


@app.route('/')
def hello_world():
    # Response('Hello World!', status=200, mimetype='text/html')
    return 'Hello World!'


@app.route('/list1/')
def list1():
    return Response('list1')


@app.route('/list2/')
def list2():
    return 'list2', 200, {'X-NAME': 'hython'}


@app.route('/list3/')
def list3():
    return {'name': 'zhilaio', 'age': 19}


if __name__ == '__main__':
    app.run(debug=True)