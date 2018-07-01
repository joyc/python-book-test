import os

HOSTNAME = '10.211.55.4'
PORT = '3306'
DATABASE = 'icbc_demo'
USERNAME = 'root'
PASSWORD = 'root'

DB_URI = f"mysql+pymysql://{USERNAME}:{PASSWORD}@{HOSTNAME}:{PORT}/{DATABASE}?charset=utf8"

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

SECRET_KEY = os.urandom(24)
