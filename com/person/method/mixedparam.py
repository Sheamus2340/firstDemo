# coding: utf-8
# @Author: Sheamus
def func(x, y, z):
    print(x, y, z)


def func2(*args, **kwargs):
    func(*args, **kwargs)


func2(1, 2, 3)

func2(1, 2, z='value')
