from sqlalchemy import create_engine, Column, Integer, Float, String, Text, \
    func, and_, or_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
import random


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'


DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"
engine = create_engine(DB_URL)
Base = declarative_base(engine)
session = sessionmaker(engine)()


# 父表user/从表article

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True, autoincrement=True)
    username = Column(String(50), nullable=False)

    # 可以被relationship参数backref取代
    # articles = relationship("Article") 

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    content = Column(Text, nullable=False)
    # 默认约束就是ondelete="RESTRICT"，不用添加。
    uid = Column(Integer, ForeignKey("user.id", ondelete="RESTRICT"))
    
    author = relationship("User", backref="articles")

    def __repr__(self):
        return "<Article(title:%s,content:%s)>" % (self.title, self.content)


# Base.metadata.drop_all()
# Base.metadata.create_all()

# user = User(username='zhiliao')
# session.add(user)
# session.commit()

# article = Article(title='abcs',content='12345',uid=1)
# session.add(article)
# session.commit()

# 原始查找方式，未使用relationship类
# article = session.query(Article).first()
# uid = article.uid
# print(article, uid)
# user = session.query(User).get(uid)
# print(user)

# 使用relationship类
article = session.query(Article).first()
print(article.author.username)
# 查询该作者所有文章 一对多关系
user = session.query(User).first()
print(user.articles)

