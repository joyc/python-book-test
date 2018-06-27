from sqlalchemy import create_engine, Column, Integer, String, \
    ForeignKey, Table
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship


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

    def __repr__(self):
        return "<User(username:%s)>" % self.username

class Article(Base):
    __tablename__ = 'article'
    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String(50), nullable=False)
    # nullable：False限制ORM无视外键约束的删除数据，报错
    uid = Column(Integer, ForeignKey("user.id"), nullable=False)

    author = relationship("User", backref="articles")

    def __repr__(self):
        return "<Article(title:%s)>" % self.title

# Base.metadata.drop_all()
# Base.metadata.create_all()

# user = User(username="erdan")
# article = Article(title='hello world')
# article.author = user
# session.add(article)
# session.commit()

# ORM层面会忽略外键约束比如默认的ondelete="RESTRICT",会被删除掉数据
# 使用nullable=False会限制这种删除
# user = session.query(User).first()
# session.delete(user)
# session.commit()

