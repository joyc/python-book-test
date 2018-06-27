from sqlalchemy import create_engine, Column, Integer, Float, String, Text, \
    func, and_, or_, ForeignKey
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
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
    
    # 设置一对一关系，需要在父模型中用uselist关闭列表属性
    # extend = relationship("UserExtend", uselist=False)

    def __repr__(self):
        return "<User(username:%s)>" % self.username


class UserExtend(Base):
    __tablename__ = 'user_extend'
    id = Column(Integer, primary_key=True, autoincrement=True)
    school = Column(String(50))
    uid = Column(Integer, ForeignKey("user.id"))

    # user = relationship("User", backref="extend")
    # 下面这句可以省略User类中的 relationship定义，需要引入orm.backref方法
    user = relationship("User", backref=backref("extend", userlist=False)


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


Base.metadata.drop_all()
Base.metadata.create_all()

# 一个user添加多个article
user = User(username='zhiliaoke')

article1 = Article(title='1234', content="abm")
article2 = Article(title="2344", content ="adkl")


user.articles.append(article1)
user.articles.append(article2)

session.add(user)
session.commit()

# 一个article添加user
user = User(username='Erdan-san')
article1 = Article(title='user article', content="xxx")
article1.author = user
session.add(article1)
session.commit()