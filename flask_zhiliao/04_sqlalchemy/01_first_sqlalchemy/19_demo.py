from sqlalchemy import create_engine, Column, Integer, String, DateTime, Enum, \
    ForeignKey, Table, func
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship, backref
from datetime import datetime


HOSTNAME = '10.211.55.4'
PORT = '3306'
DATABASE = 'flask_sqlalchemy'
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
    city = Column(String(10), nullable=False)
    age = Column(Integer, default=0)

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
        return f"<Article(title:{self.title})>"


def db_init():
    Base.metadata.drop_all()
    Base.metadata.create_all()


def add_data():
    user1 = User(username="二蛋", city="北京", age=18)
    user2 = User(username="三蛋", city="北京", age=19)
    user3 = User(username="四蛋", city="保山", age=20)
    user4 = User(username="大蛋", city="邢台", age=22)
    session.add_all([user1, user2, user3, user4])
    session.commit()


def search_user():
    # 找到跟二蛋同岁且在同一城市的人

    # 原始不效率的查询
    # user = session.query(User).filter(User.username == '二蛋').first()
    # users = session.query(User).filter(User.city == user.city, User.age == user.age).all()
    # print(users)

    # 推荐的子查询
    subq = session.query(User.city.label("city"), User.age.label("age")).filter(User.username == "二蛋").subquery()
    result = session.query(User).filter(User.city == subq.c.city, User.age == subq.c.age).all()
    print(result)


if __name__ == '__main__':
    # db_init()
    # add_data()
    search_user()
