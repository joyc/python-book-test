from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from models import User
from exts import db
from ICBC import app


manager = Manager(app)
Migrate(app, db)

manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
