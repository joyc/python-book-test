from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'


# dialect+driver://username:password@host:port/database
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

engine = create_engine(DB_URI)

# 继承SQLAlchemy基类创建ORM模型并跟表中字段意义映射，最后映射到数据库
# 创建Base元类用于被子类继承
Base = declarative_base(engine)


class Person(Base):
    __tablename__ = 'person'
    # Column来创建数据表中的对应字段
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(50))
    age = Column(Integer)
    country = Column(String(10))

# 将类对象映射到数据库
Base.metadata.create_all()
