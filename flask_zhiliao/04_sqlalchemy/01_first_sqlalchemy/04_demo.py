# encoding: utf-8
# py3中才有的枚举块
import enum
from sqlalchemy import create_engine, Column, Integer, String, \
    Float, Boolean, DECIMAL, Enum, Date, DateTime, Time
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'


DB_URL = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

engine = create_engine(DB_URL)

Base = declarative_base(engine)

session = sessionmaker(engine)()


class TagEnum(enum.Enum):
    python = "Python"
    flask = "Flask"
    django = "Django"


class Article(Base):
    """docstring for Article"""
    __tablename__ = 'article'
    id = Column(Integer,primary_key=True,autoincrement=True)
    # price = Column(Float)
    price2 = Column(DECIMAL(10, 4))
    is_delete = Column(Boolean)
    # tag = Column(Enum("Python", "Flask", "Django"))
    tag = Column(Enum(TagEnum))  # py3
    # create_time = Column(Date)
    # create_time = Column(DateTime)
    create_time = Column(Time)


Base.metadata.drop_all()  # 只删除绑定的对象的表
# 只有alembic/flask-migrate 数据迁移可以更新表结构
Base.metadata.create_all()

# article = Article(price=10.29356)
# article = Article(is_delete=True)
# article = Article(tag="python")
# article = Article(tag=TagEnum.python)  # py3 enum

# from datetime import date
# article = Article(create_time=date(2018, 6, 26))

# from datetime import datetime
# article = Article(create_time=datetime(2018,6,26,11,11,11))

from datetime import time
article = Article(create_time=time(hour=12,minute=12,second=22))
session.add(article)
session.commit()
