from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
    ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'

DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
engine = create_engine(DB_URL)
Base = declarative_base(engine)
session = sessionmaker(engine)()


class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    create_time = Column(DateTime, nullable=False, default=datetime.now)

    # 定义排序方法
    __mapper_args__ = {
        "order_by": create_time.desc()
    }

    def __repr__(self):
        return "<Article(title:%s, create_time:%S)>" % (self.title, self.create_time)

# def my_init_db():
#     Base.metadata.drop_all()
#     Base.metadata.create_all()
#     # 添加测试数据
#     user = User(username="erdan")
#     article = Article(title='hello cascade erdan')
#     article.author = user
#     session.add(article)
#     session.commit()

# def operation():
#     # article = session.query(Article).first()
#     # session.delete(article)
#     user = User(id=1, username="kenan")
#     session.merge(user)
#     session.commit()

# if __name__ == '__main__':
#     # my_init_db()
#     operation()

# 正序排序
articles = session.query(Article).order_by(Article.create_time).all()
articles = session.query(Article).order_by("create_time").all()
print(articles)
# 倒序排序
articles = session.query(Article).order_by(Article.create_time.desc).all()
articles = session.query(Article).order_by("-create_time").all()