from sqlalchemy import create_engine, Column, Integer, Float, String, \
    func, and_, or_
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import random


HOSTNAME = '10.211.55.4'
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
    id = Column()


class Article(Base):
    pass
