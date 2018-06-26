from sqlalchemy import create_engine, Column, Integer, DateTime, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from datetime import datetime


HOSTNAME = '10.211.55.4'
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


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    read_count = Column(Integer, default=10)
    # create_time = Column(DateTime)  # 1
    create_time = Column(DateTime, default=datetime.now)  # 2
    title = Column(String(30), nullable=False)
    telphone = Column(String(11), unique=True)
    # onupdate参数可以设置只在更新时候更新值
    update_time = Column(DateTime, onupdate=datetime.now, default=datetime.now)


Base.metadata.drop_all()
Base.metadata.create_all()

article = Article()
# article.create_time = datetime.now()  # 1
# article.title = 'buweikong'
# article.telphone = '1392567899'
article.title = '123'
# article = session.query(Article).first()
# session.add(article)
session.commit()
