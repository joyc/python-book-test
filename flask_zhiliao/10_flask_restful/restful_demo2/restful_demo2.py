from flask import Flask
import config
from exts import db
from models import Article, User, Tag
from articleviews import article_bp


app = Flask(__name__)
app.config.from_object(config)
# api = Api(app)
db.init_app(app)
app.register_blueprint(article_bp)

# class Article(object):
#     def __init__(self, title, content):
#         self.title = title
#         self.content = content


# article = Article(title='abc', content='xxxx')


# class ArticleView(Resource):

#     resource_fields = {
#         "title": fields.String,
#         "content": fields.String
#     }

#     @marshal_with(resource_fields)
#     def get(self):
#         return article


# api.add_resource(ArticleView, '/article/', endpoint='article')


@app.route('/')
def hello_world():
    user = User(username='zhiliao', email='sss@qq.com')
    article = Article(title='title abc', content='test 123')
    article.author = user
    tag1 = Tag(name='FrontEnd')
    tag2 = Tag(name='Python')
    article.tags.append(tag1)
    article.tags.append(tag2)
    db.session.add(article)
    db.session.commit()
    return 'hello world'


if __name__ == '__main__':
    app.run(debug=True)
