from sqlalchemy import create_engine

HOSTNAME = '127.0.0.1'
PORT = '3306'
DATABASE = 'first_sqlalchemy'
USERNAME = 'root'
PASSWORD = 'root'


# dialect+driver://username:password@host:port/database
DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

engine = create_engine(DB_URI)

# 判断是否连接成功
conn = engine.connect()
result = conn.execute('select 1')
print(result.fetchone())


# 使用with连接数据如果异常会被捕获
with engine.connect() as con:
    # 删除user表
    con.execute('drop table if exists users')
    # 创建user表
    con.execute('create table users(id int primary key auto_increment,'
                'name varchar(25))')
    # 插入数据
    con.execute('insert into users(name) values("xiaoming")')
    con.execute('insert into users(name) values("erdan")')
    # 执行查询
    rs = con.execute('select * from users')
    # 遍历查找结果
    for row in rs:
        print(row)
