# coding: utf-8
# @Author: Sheamus
# *形参名
# 处理逻辑，多的参数会封装成元组，然后赋值给变量
def func(x, *args):
    print(x, args)


func(1, 2, 3)  # y = (2, 3)
func(1, 2, 3, 4)  # y = (2, 3, 4)


def func(x, y, **kwargs):
    print(x, y, kwargs)


func(1, 2, a=1, b=2, c=3)

func(1, y=2, a=1, b=2)


def func(x, *args):
    print(x, args)


age = [1, 2, 3]
func(1, *age)

func(*"愿望终将实现")


def func(x, **kwargs):
    print(x, kwargs)


dic = {'x': 1, 'y': 2}
func(**dic)
