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


# 包装成response可以设置cookie，session等
@app.route('/list4/')
def list4():
    resp = Response('list4')
    resp.set_cookie('country', 'china')
    return resp


if __name__ == '__main__':
    app.run(debug=True)

"""
### 视图函数中可以返回哪些值：
1. 可以返回字符串：返回的字符串其实底层将这个字符串包装成了一个`Response`对象。
2. 可以返回元组：元组的形式是(响应体,状态码,头部信息)，也不一定三个都要写，写两个也是可以的。返回的元组，其实在底层也是包装成了一个`Response`对象。
3. 可以返回`Response`及其子类。


### 实现一个自定义的`Response`对象：
1. 继承自`Response`类。
2. 实现方法`force_type(cls,rv,environ=None)`。
3. 指定`app.response_class`为你自定义的`Response`对象。
4. 如果视图函数返回的数据，不是字符串，也不是元组，也不是Response对象，那么就会将返回值传给`force_type`，然后再将`force_type`的返回值返回给前端。
"""