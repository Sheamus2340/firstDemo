# coding: utf-8
# @Author: Sheamus

# with open('data/c.txt', mode='wb') as f1:
#     f1.write('清风徐来'.encode('utf-8'))
#
# with open('data/c.txt', mode='rb') as f2:
#     res = f2.read()
#     print(res)

# with open('data/a.txt', mode='rb') as f3, \
#         open('data/d.txt', mode='wb') as f4:
#     for line in f3:
#         f4.write(line)

with open('data/a.txt', mode='rb') as f3, \
        open('data/e.txt', mode='wb') as f4:
    while 1:
        res = f3.read(1024)
        if not res:
            break
        f4.write(res)
        print(res)

print(b'man')
print('人'.encode('utf-8'))
print(bytes('人', encoding='utf-8'))
