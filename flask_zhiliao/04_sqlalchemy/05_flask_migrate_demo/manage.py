from flask_script import Manager
from zhiliao import app
from exts import db
from flask_migrate import Migrate, MigrateCommand
# 需要把映射到数据库中的模型导入到manager.py中
from models import User


manager = Manager(app)
Migrate(app, db)
manager.add_command("db", MigrateCommand)


if __name__ == '__main__':
    manager.run()
