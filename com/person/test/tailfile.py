# coding: utf-8
# @Author: Sheamus

with open('data/user.log', mode='rt', encoding='utf-8') as file:
    while 1:
        res = file.readline()
        if res:
            print(res.strip())
