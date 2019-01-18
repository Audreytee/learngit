# 配置文件当中的值最好大写，类似于全局变量
# 数据库、密码、
# 生产环境的相关配置

DEBUG = False

# cymysql:引擎
# sqlalchemy 支持分布式的数据库

SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://root:123@localhost:3306/fisher?charset=utf8'

SQLALCHEMY_TRACK_MODIFICATIONS = True
SQLALCHEMY_COMMIT_TEARDOWN = True

# email seting
MAIL_SERVER = 'smtp.qq.com'
MAIL_PORT = 465
MAIL_USE_SSL = True
MAIL_USE_TSL = False
MAIL_USERNAME = '2944998544@qq.com'
MAIL_PASSWORD = '123456'
MAIL_SUBJECT_PREFIX = '[鱼书]'
MAIL_SENDER = '鱼书<hello@yushu.im>'
