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


#### jinjia2控制结构

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
| content | 用户定义的页面内容 | 
| scripts | 文档底部的 JavaScript 声明| 

#### url_for生成链接
url_for() 函数最简单的用法是以视图函数名（或者`app.add_url_route()`)定义路由时使用的端点名作为参数，返回对应的URL。
当前hello.py 程序中调用`url_for('index')`得到的结果是`/`。

`url_for('index', _external=True)` 
返回的则是绝对地址，在这个示例中是`http://localhost:5000/`。

使用`url_for()`生成动态地址时，将动态部分作为关键字参数传入。
例如，`url_for('user', name='john', _external=True)` 
的返回结果是 `http://localhost:5000/user/john`。 
传入`url_for()`的关键字参数不仅限于动态路由中的参数。
函数能将任何额外参数添加到 查询字符串中。
例如，`url_for('index', page=2)`的返回结果是`/?page=2`。

#### 静态文件static
查看url映射时，其中有一个`static`路由。 
这是因为对静态文件的引用被当成一个特殊的路由，
即`/static/<filename>`。
例如，调用`url_for('static', filename='css/styles.css', _external=True)` 
返回 `http:// localhost:5000/static/css/styles.css`。

默认设置下，Flask 在程序根目录中名为 static 的子目录中寻找静态文件。
如果需要，可在 static 文件夹中使用子文件夹存放文件。
服务器收到前面那个 URL 后，会生成一个响应， 包含文件系统中 static/css/styles.css 文件的内容。

#### 使用Flask-Moment本地化日期和时间


## web表单


## 数据库
### ORM、ODM的使用
#### FLask-SQLAlchemy

##### FLask-SQLAlchemy数据库URL

|数据库引擎| URL|
|--|--|
|MySQL| mysql://username:password@hostname/database|
|Postgres| postgresql://username:password@hostname/database|
|SQLite（Unix）| sqlite:////absolute/path/to/database|
|SQLite（Windows）| sqlite:///c:/absolute/path/to/database|

程序使用的数据库URL必须保存到Flask配置对象的`SQLALCHEMY_DATABASE_URI`键中。配置对象中还有一个很有用的选项，即`SQLALCHEMY_COMMIT_ON_TEARDOWN`键，将其设为`True`时，每次请求结束后都会自动提交数据库中的变动。


##### 常用的SQLAlchemy列类型

| 类型名 | Python类型 | 说　　明|
|--|--|--|
| Integer | int | 普通整数，一般是 32 位| 
| SmallInteger | int | 取值范围小的整数，一般是 16 位| 
| BigInteger | int 或 long | 不限制精度的整数| 
| Float | float | 浮点数| 
| Numeric | decimal.Decimal | 定点数| 
| String | str | 变长字符串| 
| Text | str | 变长字符串，对较长或不限长度的字符串做了优化| 
| Unicode | unicode | 变长 Unicode 字符串| 
| UnicodeText | unicode | 变长 Unicode字符串，对较长或不限长度的字符串做了优化| 
| Boolean | bool | 布尔值| 
| Date | datetime.date | 日期| 
| Time | datetime.time | 时间| 
| DateTime | datetime.datetime | 日期和时间| 
| Interval | datetime.timedelta | 时间间隔| 
| Enum | str | 一组字符串| 
| PickleType | 任何 Python 对象 | 自动使用 Pickle 序列化| 
| LargeBinary | str | 二进制文件| 

db.Column 中其余的参数指定属性的配置选项:

##### 常使用的SQLAlchemy列选项
| 选项名 | 说　　明 |
| -- | -- |
|primary_key | 如果设为True ，这列就是表的主键|
|unique |如果设为True，这列不允许出现重复的值|
|index |如果设为True，为这列创建索引，提升查询效率|
|nullable |如果设为True，这列允许使用空值；如果设为False，这列不允许使用空值|
|default |为这列定义默认值|

### 关系

#### 一对多关系在模型类中的表示方法

```py
class Role(db.Model):
    # ...
    users = db.relationship('User', backref='role')

class User(db.Model):
    # ...
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
```

##### 常用的SQLAlchemy关系选项
- backref
    在关系的另一个模型中添加反向引用
- primaryjoin
    明确指定两个模型之间使用的联结条件。只在模棱两可的关系中需要指定
- lazy
    指定如何加载相关记录。可选值有 select （首次访问时按需加载）、 immediate （源对象加载后就加载）、 joined （加载记录，但使用联结）、 subquery （立即加载，但使用子查询），noload （永不加载）和 dynamic （不加载记录，但提供加载记录的查询）
- uselist 
    如果设为 Fales ，不使用列表，而使用标量值
- order_by 
    指定关系中记录的排序方式
- secondary 
    指定多对多关系中关系表的名字
- secondaryjoin 
    SQLAlchemy 无法自行决定时，指定多对多关系中的二级联结条件

> 一对一关系可以用前面介绍的一对多关系表示，但调用 db.relationship() 时要把 uselist 设为 False ，把“多”变成“一”。多对一关系也可使用一对多表示，对调两个表即可，或者把外键和 db.relationship() 都放在“多”这一侧。最复杂的关系类型是多对多，需要用到第三张表，这个表称为关系表。

##### 常用的SQLAlchemy查询过滤器

| 过滤器 | 说　　明 |
| -- | -- |
| filter() | 把过滤器添加到原查询上，返回一个新查询 |
| filter_by() | 把等值过滤器添加到原查询上，返回一个新查询 |
| limit() | 使用指定的值限制原查询返回的结果数量，返回一个新查询 |
| offset() | 偏移原查询返回的结果，返回一个新查询 |
| order_by() | 根据指定条件对原查询结果进行排序，返回一个新查询 |
| group_by() | 根据指定条件对原查询结果进行分组，返回一个新查询 |

##### 常使用的SQLAlchemy查询执行函数

| 方　法 | 说　　明 |
| -- | -- |
| all() | 以列表形式返回查询的所有结果 |
| first() | 返回查询的第一个结果，如果没有结果，则返回 None |
| first_or_404() | 返回查询的第一个结果，如果没有结果，则终止请求，返回 404错误响应 |
| get() | 返回指定主键对应的行，如果没有对应的行，则返回 None |
| get_or_404() | 返回指定主键对应的行，如果没找到指定的主键，则终止请求，返回404 错误响应 |
| count() | 返回查询结果的数量 |
| paginate() | 返回一个Paginate对象，它包含指定范围内的结果 |


可以通过Flask shell调试

增加shell回调方法 省去每次输入实例
```py
from flask_script import Manager, Shell

def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role)
manager.add_command('shell', Shell(make_context=make_shell_context))
```

### Flask-Migrate实现数据库迁移

这个扩展对`Alembic`做了轻量级包装，并集成到`Flask-Script`中，所有操作都通过`Flask-Script`命令完成。

为了导出数据库迁移命令，Flask-Migrate 提供了一个 MigrateCommand 类，可附加到 Flask-
Script 的 manager 对象上。在这个例子中， MigrateCommand 类使用 db 命令附加。在维护数据库迁移之前，要使用 init 子命令创建迁移仓库:
```py
python hello.py db init
```

