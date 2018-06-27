from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

HOSTNAME = '10.211.55.4'
PORT = '3306'
DATABASE = 'flask_sqlalchemy_demo'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

app.config['SQLALCHEMY_DATABASE_URI'] = DB_URI
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)


class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(50), nullable=False)


class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(50), nullable=False)
    uid = db.Column(db.Integer, db.ForeignKey("user.id"))

    author = db.relationship("User", backref="articles")


# db.drop_all()
# db.create_all()

# user = User(username='erdan')
# article = Article(title='title one world')
# cascade save-update
# article.author = user
#
# db.session.add(article)
# db.session.commit()

# order_by filter filter_by group_by join
# users = User.query.all()
users = User.query.order_by(User.id.desc()).all()
print(users)


@app.route('/hello_world')
def hello_world():
    return 'Hello World!'


if __name__ == '__main__':
    app.run()
