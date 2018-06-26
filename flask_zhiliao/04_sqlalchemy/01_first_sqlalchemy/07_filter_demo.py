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


class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    price = Column(Float, nullable=False)
    content = Column(String(100))

    def __repr__(self):
        return "<Article(title: %s)>" % self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()

# session.query(Article).filter(Article.id == 1)
# session.query(Article).filter_by(id=1)

# equal
# article = session.query(Article).filter(Article.title == "title3").first()
# print(article)

# not equal
# article = session.query(Article).filter(Article.title != "title3").all()
# print(article)

# like & ilike(不区分大小写)
# articles = session.query(Article).filter(Article.title.like('title%')).all()
# print(articles)

# in 区别于buildin的 in方法 取名为in_
# article = session.query(Article).filter(Article.title.in_(['title1', 'title2'])).all()
# print(article)

# not in 用取反的 ~ 或者 notin_
# article = session.query(Article).filter(~Article.title.in_(['title1', 'title2'])).all()
# article = session.query(Article).filter(Article.title.notin_(['title1', 'title2'])).all()
# print(article)

# is null
# articles = session.query(Article).filter(Article.content == None).all()
# print(articles)

# is not null
# articles = session.query(Article).filter(Article.content != None).all()
# print(articles)

# and 或者导入并使用 and_
# articles = session.query(Article).filter(Article.title=='abc', Article.content=='abc').all()
# articles = session.query(Article).filter(and_(Article.title=='abc', Article.content=='abc')).all()
# print(articles)

# or
articles = session.query(Article).filter(or_(Article.title, Article.content)).all()
print(articles)
