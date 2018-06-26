from sqlalchemy import create_engine, Column, Integer, Float, String, \
    func
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

    def __repr__(self):
        return "<Article(title: %s)>" % self.title


# Base.metadata.drop_all()
# Base.metadata.create_all()

# 加入测试数据
# for x in range(1, 7):
#     article = Article(title=f'title{x}', price=random.randint(1, 100))
#     session.add(article)
# session.commit()

# 查询模型对象
articles = session.query(Article).all()
# for article in articles:
#     print(article)
print(articles)

# 查询模型中的属性
articles = session.query(Article.title, Article.price).all()
print(articles)

# 聚合函数
count = session.query(func.count(Article.id)).first()
print(count)
avg = session.query(func.avg(Article.price)).first()
print(avg)
maxvalue = session.query(func.max(Article.price)).first()
print(maxvalue)
sum = session.query(func.sum(Article.price)).first()
print(sum)
