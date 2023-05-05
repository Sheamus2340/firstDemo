# coding: utf-8
# @Author: Sheamus
def append_one(x, y, l=[]):
    l.append(x)
    l.append(y)
    print(l)


names = [4, 5]
# 此时就意外的输出了 4，5，1，2
append_one(1, 2, names)


def append_my(x, y, name=None):
    if name is None:
        name = []
    name.append(x)
    name.append(y)
    print(name)


append_my(1, 2, [1, 2, 3])
