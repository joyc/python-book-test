# encoding: utf-8
import os

SECRET_KEY = os.urandom(24)

DEBUG = True

DB_USERNAME = 'root'
DB_PASSWORD = 'root'
DB_HOST = '10.211.55.4'
# DB_HOST = '127.0.0.1'
DB_PORT = '3306'
DB_NAME = 'zlbbs'

# PERMANENT_SESSION_LIFETIME =

DB_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}?charset=utf8"

SQLALCHEMY_DATABASE_URI = DB_URI
SQLALCHEMY_TRACK_MODIFICATIONS = False

CMS_USER_ID = 'cms_user_id_xxx'

# 发送者邮箱服务器地址
MAIL_SERVER = "smtp.gmail.com"
MAIL_PORT = 587
MAIL_USE_TLS = True
# MAIL_USE_SSL = default False
MAIL_USERNAME = "xxx@gmail.com"
MAIL_PASSWORD = "xxx"
MAIL_DEFAULT_SENDER = "xxx@gmail.com"
