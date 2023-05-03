# coding: utf-8
# @Author: Sheamus

with open('data/a.txt', mode='wt', encoding='utf-8') as file:
    file.write('清风徐来\n')
    file.write('水波不兴\n')

with open('data/a.txt', mode='at', encoding='utf-8') as file:
    file.write('王菲'.center(50, '-'))

with open('data/a.txt', mode='rt', encoding='utf-8') as file:
    for line in file:
        print(line, end='')

# 文件的拷贝能力实现
with open('data/a.txt', mode='rt', encoding='utf-8') as f1, \
        open('data/b.txt', mode='wt', encoding='utf-8') as f2:
    f2.write(f1.read())

print()

with open('data/a.txt', mode='rt', encoding='utf-8') as file:
    for line in file:
        print(line.strip())
    else:
        print('perfect')

