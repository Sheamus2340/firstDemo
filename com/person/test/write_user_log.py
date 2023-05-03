# coding: utf-8
# @Author: Sheamus

with open('data/user.log', mode='at', encoding='utf-8') as file:
    while 1:
        context = input("输入你想说的话>>>>\n")
        if context == 'Q':
            break
        file.write(f'{context}\n')
        file.flush()
