"""
 Created by yan on 2018/8/30 17:39
"""
__author__ = 'yan'

from flask import Flask,current_app,request,Request

app = Flask(__name__)

# Flask AppContext
# Request RequestContext
ctx = app.app_context()
ctx.push()
a = current_app
print(current_app)  # RuntimeError: Working outside of application context.
ctx.pop()

# with app.app_context():
#     a = current_app
#     d = current_app.config['DEBUG']

# 实现了上下文协议的对象使用
# 上下文管理器
# __enter__ __exit__
# 返回上下文管理器


class MyResource:
    def __enter__(self):
        print('connect to resource')
        return self

    def __exit__(self, exc_type, exc_value, tb):
        if tb:
            print('process execption')
        else:
            print('no exception')
        print('close to resource')
        return False

    def query(self):
        print('query data')


try:
    with MyResource() as resource:
        1/0
        resource.query()
except Exception as ex:
    pass
# 连接数据库
# sql
# 释放资源
