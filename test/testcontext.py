class MyResource():
    # def __enter__(self):
    #     print('enter resource.....')
    #     return self
    #
    # def __exit__(self, exc_type, exc_val, exc_tb):
    #     print('closing resource....')

    def query(self):
        print('query data')


# with MyResource() as r:
#     r.query()

from contextlib import contextmanager

# 把不是上下文的类变成上下文管理器
@contextmanager
def make_myresource():
    print('enter resources...')
    yield MyResource()
    print('close resources ....')


# yield 生成器
with make_myresource() as r:
    r.query()
