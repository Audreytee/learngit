# IO密集型的程序 查询数据库,请求网络资源,读写文件
# flask web 框架
# 请求,线程
# flask 开启多少个线程来处理请求
# nginx apache tomact iis

# 线程隔离 werkzeug local Local dict
# localstack local 使用字典的实现的线程隔离
# 线程隔离的栈结构

# {thread_id1:Lvalue1,thread_id2:value2...}
# 封装
from werkzeug.local import Local
import threading
import time

my_obj=Local()
my_obj.b=1


def worker():
    my_obj.b=2
    print('in new thread b is:'+str(my_obj.b))

#new thread
new_t=threading.Thread(target=worker, name='qiyue_thread')
new_t.start()
time.sleep(1)
# main thread
print('in main thread b is:'+str(my_obj.b))
