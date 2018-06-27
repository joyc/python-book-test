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
    age = Column(Integer, default=20)
    gender = Column(Enum("male", "female", "secret"), default="male")

    def __repr__(self):
        return "<User(username:%s)>" % self.username


def db_init():
    Base.metadata.drop_all()
    Base.metadata.create_all()

def add_data():
    user1 = User(username="erdan", age=18, gender="female")
    user2 = User(username="sandan", age=19, gender="male")
    user3 = User(username="sidan", age=20, gender="female")
    user4 = User(username="wudan", age=21, gender="male")
    user5 = User(username="dadan", age=22, gender="secret")
    session.add_all([user1, user2, user3, user4, user5])
    session.commit()


def search_user():
    #每个年龄段人数
    # result = session.query(User.age, func.count(User.id)).group_by(User.age).all()
    # print(result)
    #大于20的，用having对结果再次过滤
    result = session.query(User.age, func.count(User.id)).group_by(User.age) \
            .having(User.age > 20).all()
    print(result)

if __name__ == '__main__':
    # db_init()
    # add_data()
    search_user()
