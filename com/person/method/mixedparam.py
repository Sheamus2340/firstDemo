# coding: utf-8
# @Author: Sheamus
def func(x, y, z):
    print(x, y, z)


def func2(*args, **kwargs):
    print(f'打印形参的数据是什么: {args} ,{kwargs}')  # 打印形参的数据是什么
    func(*args, **kwargs)


func2(1, 2, 3)

func2(1, 2, z='value')


def func3(**kwargs):
    print(kwargs)


dict_test = {'a': 1}
func3(**dict_test)


def func4(a):
    print(a)


func4(**dict_test)
