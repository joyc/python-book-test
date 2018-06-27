from sqlalchemy import create_engine, Column, Integer, String, DateTime, \
    ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
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
    uid = Column(Integer, ForeignKey("user.id"))
    # lazy=dynamic 可以指定返回的不是查询结果列表而是查询对象，也就是sql语句
    author = relationship("User", backref=backref("articles", lazy='dynamic'))

    def __repr__(self):
        return "<Article(title:%s)>" % (self.title)


def db_init():
    Base.metadata.drop_all()
    Base.metadata.create_all()

def add_data():
    user = User(username="erdan")
    for x in range(1,100):
        article = Article(title=f"title {x}")
        article.author = user
        session.add(article)
    session.commit()

def serach_article():
    user = session.query(User).first()
    # print(user.articles)
    # new_post = user.articles.filter(Article.id > 50).all()
    # print(new_post)
    # 可以继续添加数据
    user.articles.append(Article(title="title 100"))
    session.commit()


if __name__ == '__main__':
    # db_init()
    # add_data()
    serach_article()
