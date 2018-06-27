from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum, \
    ForeignKey, Table, func
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
    
    author = relationship("User", backref="articles")

    def __repr__(self):
        return "<Article(title:%s)>" % (self.title)


def db_init():
    Base.metadata.drop_all()
    Base.metadata.create_all()

def add_data():
    user1 = User(username="erdan")
    user2 = User(username="sandan")
    for x in range(1):
        article = Article(title='title %s' % x)
        article.author = user1
        session.add(article)
    session.commit()

    for x in range(1, 3):
        article = Article(title='title %s' % x)
        article.author = user2
        session.add(article)
    session.commit()

def search_user():
    #找到所有用户按照发表的文章数量排序
    result = session.query(User.username, func.count(Article.id)).join(Article,
    User.id==Article.uid).group_by(User.id).order_by(func.count(Article.id).desc()).all()
    print(result)

if __name__ == '__main__':
    # db_init()
    # add_data()
    search_user()
