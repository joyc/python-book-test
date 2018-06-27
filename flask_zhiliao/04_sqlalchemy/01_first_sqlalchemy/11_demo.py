from sqlalchemy import create_engine, Column, Integer, Float, String, Text, \
    func, and_, or_, ForeignKey, Table
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

# 导入table类创建多对多关系中的中间表
article_tag = Table(
    "article_tag",
    Base.metadata,
    Column("article_id", Integer, ForeignKey("article.id"), primary_key=True),
    Column("tag_id", Integer, ForeignKey("tag.id"), primary_key=True)
)

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)

    tags = relationship("Tag", backref="articles", secondary="article_tag")

    def __repr__(self):
        return "<Article(title:%s)>" % (self.title)


class Tag(Base):
    __tablename__ = 'tag'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50), nullable=False)

    def __repr__(self):
            return "<Tag(name:%s)>" % (self.name)

# 测试数据
# Base.metadata.drop_all()
# Base.metadata.create_all()

# article1 = Article(title="article1 title")
# article2 = Article(title="article2 title")

# tag1 = Tag(name="tag1")
# tag2 = Tag(name="tag2")

# article1.tags.append(tag1)
# article1.tags.append(tag2)

# article2.tags.append(tag1)
# article2.tags.append(tag2)

# session.add(article1)
# session.add(article2)

# session.commit()

# 查询文章的所有tag
article = session.query(Article).first()
print(article.tags)
# 查询tag下所有文章
tag = session.query(Tag).first()
print(tag.articles)