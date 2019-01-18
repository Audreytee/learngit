import threading
import time


def worker():
    print('i am july')
    t = threading.current_thread()
    time.sleep(8)
    print(t.getName())


# 启动线程
new_t=threading.Thread(target=worker, name='qiyue_thread')
new_t.start()


# 更加充分利用多核cpu的性能优势
# 异步编程
# 多核cpu 并行的执行程序
# GIL global interpreter lock 全局解释器锁
# 锁，线程安全
# 内存资源，一个进程有多个线程 共享
# 线程不安全

# 主线程
# 锁
# 细粒度的锁，程序员 主动加锁
# 粗粒度锁， 解释器锁 GIL 多核cpu 1个线程执行，一定程度上保证线程安全
# python解释器 bytecode cpython(GIL) jpython
# 多进程之间通信技术，进程之间切换成本比线程之间切换的成本要高


t=threading.current_thread()
print(t.getName())