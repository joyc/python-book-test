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

    def __repr__(self):
        return "<Article(title:%s)>" % (self.title)


def db_init():
    Base.metadata.drop_all()
    Base.metadata.create_all()

def add_data():
    for x in range(1,100):
        title = f"title {x}"
        article = Article(title=title)
        session.add(article)
    session.commit()


def search():
    # 查询全部
    # articles = session.query(Article).all()
    # limit限制
    # articles = session.query(Article).offset(10).limit(10).all()
    # articles = session.query(Article).order_by(Article.id.desc()).offset(10).limit(10).all()
    # articles = session.query(Article).order_by(Article.id.desc()).slice(0,10).all()
    articles = session.query(Article).order_by(Article.id.desc())[0:10]
    print(articles)
    # from sqlalchemy.orm.query import Query



if __name__ == '__main__':
    # db_init()
    # add_data()
    search()

    