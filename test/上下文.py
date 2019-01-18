"""
 Created by yan on 2018/9/29 14:55
"""
__author__ = 'yan'

# contextmanager把原本不是上下文管理器的类，包装成一个上下文管理器
from contextlib import contextmanager

class MyResource:
    # def __enter__(self):
    #     print('connect to resource')
    #     return self

    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print('close resource connect')
    def query(self):
        print('query data')

@contextmanager
def make_myresource():
    print('connect to resource')
    # 走到这一步，停下来，执行query，然后回来继续执行打印
    yield MyResource()
    print('close resource connect')


with make_myresource() as r:
    r.query()