# coding: utf-8
# @Author: Sheamus
from functools import wraps
import time


# 封装计时的功能

def count_time(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        resp = func(*args, **kwargs)
        end = time.time()
        print(f"执行使用时间 {end - start}")
        return resp

    return wrapper


@count_time
def recharge(num):
    for i in range(num, 101):
        time.sleep(0.05)
        print(f"\r当前充电量 {'▌' * i}  {i}%", end="")
    print()
    print("充电完成")
    return 100


res = recharge(20)

print(res)


