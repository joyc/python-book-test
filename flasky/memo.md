### Flask上下文全局变量

|变量名|上下文|说明|
|--|--|--|
|current_app |程序上下文| 当前激活程序的程序实例|
|g |程序上下文 |处理请求时用作临时存储的对象。每次请求都会重设这个变量|
|request |请求上下文 |请求对象，封装了客户端发出的 HTTP 请求中的内容|
|session |请求上下文 |用户会话，用于存储请求之间需要“记住”的值的词典|

- `app.url_map`可以查看当前Flask程序中的URL映射,如：

```py
In [17]: app.url_map
Out[17]:
Map([<Rule '/' (OPTIONS, GET, HEAD) -> index>,
 <Rule '/userid/<id>' (OPTIONS, GET, HEAD) -> user_id>,
 <Rule '/static/<filename>' (OPTIONS, GET, HEAD) -> static>,
 <Rule '/user/<name>' (OPTIONS, GET, HEAD) -> user>])
```

### 请求钩子

请求钩子使用修饰器实现。Flask 支持以下 4 种钩子。  

- before_first_request:注册一个函数，在处理第一个请求之前运行。
- before_request:注册一个函数，在每次请求之前运行。
- after_request:注册一个函数，如果没有未处理的异常抛出，在每次请求之后运行。
- teardown_request:注册一个函数，即使有未处理的异常抛出，也在每次请求之后运行。

> 在请求钩子函数和视图函数之间共享数据一般使用上下文全局变量`g` 。例如，`before_request`处理程序可以从数据库中加载已登录用户，并将其保存到`g.user`中。随后调用视图函数时，视图函数再使用`g.user`获取用户。


- `response`和`cookie`
可以导入`make_response`并使用方法`set_cookie`来设置cookie，如下：
```py
@app.route('/')
def index():
    response = make_response('<h1>This document carries a cookie!</h1>')
    response.set_cookie('answer', '12')
    return response
```

### 使用`redirect`设置重定向

```py
from flask import redirect

@app.route('/')
def index():
    return redirect('http://g.cn')
```

### 使用jinjia2模板引擎

Jinja2 能识别所有类型的变量，甚至是一些复杂的类型，例如列表、字典和对象。
```html
<p>A value from a dictionary: {{ mydict['key'] }}.</p>
<p>A value from a list: {{ mylist[3] }}.</p>
<p>A value from a list, with a variable index: {{ mylist[myintvar] }}.</p>
<p>A value from an object's method: {{ myobj.somemethod() }}.</p>
```
可以使用过滤器修改变量，过滤器名添加在变量名之后，中间使用竖线分隔。例如，下述模板以首字母大写形式显示变量 name 的值：
`Hello, {{ name|capitalize }}`

#### Jinja2变量过滤器

完整filter参见[官方文档](http://jinja.pocoo.org/docs/2.10/templates/#filters)

|过滤器名 |说　　明|
| -- | -- |
|safe |渲染值时不转义|
|capitalize |把值的首字母转换成大写，其他字母转换成小写|
|lower |把值转换成小写形式|
|upper |把值转换成大写形式|
|title |把值中每个单词的首字母都转换成大写|
|trim |把值的首尾空格去掉|
|striptags |渲染之前把值中所有的 HTML 标签都删掉|

> 千万别在不可信的值上使用 safe 过滤器，例如用户在表单中输入的文本。


####jinjia2控制结构

```
{% if user %}
    Hello, {{ user }}!
{% else %}
    Hello, Stranger!
{% endif %}

<ul>
    {% for comment in comments %}
        <li>{{ comment }}</li>
    {% endfor %}
</ul>
```
Jinja2 还支持宏。宏类似于 Python 代码中的函数:

```py
{% macro render_comment(comment) %}
    <li>{{ comment }}</li>
{% endmacro %}
<ul>
    {% for comment in comments %}
        {{ render_comment(comment) }}
    {% endfor %}
</ul>

{% include 'common.html' %}
```

为了重复使用宏，我们可以将其保存在单独的文件中，然后在需要使用的模板中导入：

```py
{% import 'macros.html' as macros %}

<ul> 
    {% for comment in comments %}
        {{ macros.render_comment(comment) }}
    {% endfor %} 
</ul>
```

#### flask-bootstrap

Flask-Bootstrap基模板中定义的块

| 块　　名 | 说　　明 |
| -- | -- |
| doc |整个 HTML 文档 |
| html_attribs | <html> 标签的属性 | 
| html | <html> 标签中的内容 |
| head | <head> 标签中的内容 |
| title | <title> 标签中的内容 |
| metas | 一组 <meta> 标签 | 
| styles | 层叠样式表定义 | 
| body_attribs | <body> 标签的属性 | 
| body | <body> 标签中的内容 | 
| navbar | 用户定义的导航条 | 
| content 用户定义的页面内容 | 
| scripts | 文档底部的 JavaScript 声明| 

#### url_for生成链接
url_for() 函数最简单的用法是以视图函数名（或者 app.add_url_route()定义路由时使用的端点名作为参数，
返回对应的URL。
当前hello.py 程序中调用url_ for('index')得到的结果是/。

url_for('index', _external=True) 
返回的则是绝对地址，在这个示例中是 http://localhost:5000/

使用 url_for() 生成动态地址时，将动态部分作为关键字参数传入。
例如，url_for ('user', name='john', _external=True) 
的返回结果是 http://localhost:5000/user/john。 
传入 url_for() 的关键字参数不仅限于动态路由中的参数。
函数能将任何额外参数添加到 查询字符串中。
例如，url_for('index', page=2) 的返回结果是 /?page=2。

#### 静态文件static
查看url映射时，其中有一个 static 路由。 
这是因为对静态文件的引用被当成一个特殊的路由，
即 /static/<filename>。
例如，调用 url_for('static', filename='css/styles.css', _external=True) 
返回 http:// localhost:5000/static/css/styles.css。

默认设置下，Flask 在程序根目录中名为 static 的子目录中寻找静态文件。
如果需要，可在 static 文件夹中使用子文件夹存放文件。
服务器收到前面那个 URL 后，会生成一个响应， 包含文件系统中 static/css/styles.css 文件的内容。

#### 使用Flask-Moment本地化日期和时间


## web表单





