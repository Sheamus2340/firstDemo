# coding: utf-8
# @Author: Sheamus

import time


def begingame(group, s):
    print("欢迎来到王者荣耀")
    print(f"我方在{group}阵营")
    print(f"敌方还有{s}秒到达战场")
    time.sleep(3)
    print("游戏开始")


# begingame("红方", 3)

# 方案一：
# 没有破坏 begingame 函数
# 缺点：
#   1. 所有的调用方式改成了 wrapper；
#   2. 这个包装不通用，后面来了一个新的方法需要使用这个功能就不能使用了；
#
# def wrapper(group, s):
#     start = time.time()
#     begingame(group, s)
#     end = time.time()
#     print(f"使用了 {end - start}")
#
#
# wrapper("红方", 3)

# 方案二：
# 解决了通用的问题，但是没有解决调用方式的问题

# func = begingame
# def wrapper(*args, **kwargs):
#     start = time.time()
#     func(*args, **kwargs)
#     end = time.time()
#     print(f"使用了 {end - start}")

# 方案三：把通用和调用方式都解决了，这个就是装饰器

def outer(func):
    def wrapper(*args, **kwargs):
        start = time.time()
        func(*args, **kwargs)
        end = time.time()
        print(f"使用了 {end - start}")

    return wrapper


print(f"运行前的函数地址：{begingame}")

# 返回的函数名称又赋值给原函数名
begingame = outer(begingame)

print(f"现在的函数地址：{begingame}")
begingame("红方", 3)
