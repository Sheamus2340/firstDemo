# coding: utf-8
# @Author: Sheamus

# 方式一：将内容全部加载到内存，修改，然后覆盖原内容写入
with open('data/f.txt', mode='rt', encoding='utf-8') as f1:
    res = f1.read()
    newres = res.replace('----', '****')

with open('data/f.txt', mode='wt', encoding='utf-8') as f2:
    f2.write(newres)

# 方式二：一行一行的修改，写在一个新的临时文件文件中，结束了删除源文件，重命名临时文件为原文件名
import os

with open('data/g.txt', mode='rt', encoding='utf-8') as f1, \
        open('data/g.txt.swap', mode='wt', encoding='utf-8') as f2:
    while 1:
        res = f1.readline()
        if not res:
            break
        # f2.write(res.replace('****', '----'))
        f2.write(res.replace('----', '****'))

os.remove('data/g.txt')
os.renames('data/g.txt.swap', 'data/g.txt')
