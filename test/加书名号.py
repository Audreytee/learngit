"""
 Created by yan on 2018/9/29 15:15
"""
__author__ = 'yan'

from contextlib import contextmanager

# contextmanager把原本不是上下文管理器的类，包装成一个上下文管理器
@contextmanager
def book_mark():
    print('《',end='')
    yield
    print('》')


with book_mark():
    print('且将生活一饮而尽',end='')
