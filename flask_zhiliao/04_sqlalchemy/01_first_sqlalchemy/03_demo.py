#encoding: utf-8

from sqlalchemy import create_engine, Column, Integer, String
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

# Session = sessionmaker(engine)
# session = Session()
session = sessionmaker(engine)()


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer,primary_key=True,autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    country = Column(String(50))

    def __str__(self):
        return f"<Person(name:{self.name},age:{self.age},country:{self.country})>"


# session会话
# 增加
def add_data():
    p1 = Person(name='erdan1',age=18,country='china')
    p2 = Person(name='erdan2',age=20,country='japan')
    session.add_all([p1, p2])
    session.commit()


# 查询
def search_data():
    # all_person = session.query(Person).all()
    # for p in all_person:
    #     print(p)
    # all_person = session.query(Person).filter_by(name='zhiliao').all()
    # for x in all_person:
    #     print(x)
    # all_person = session.query(Person).filter(Person.name=='zhiliao').all()
    # for x in all_person:
    #     print(x)
    person = session.query(Person).first()
    print(person)    

# 修改
def update_data():
    person = session.query(Person).first()
    person.name = 'ketang'
    session.commit()

# 删除
def delete_data():
    person = session.query(Person).first()
    session.delete(person)
    session.commit()


if __name__ == '__main__':
    # add_data()
    # search_data()
    # update_data()
    delete_data()   
