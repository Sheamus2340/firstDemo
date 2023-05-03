# coding: utf-8
# @Author: Sheamus

# with open('data/user.log', mode='a+t', encoding='utf-8') as file:
#     while 1:
#         res = file.readline()
#         if res:
#             print(res.strip())

# import time
# with open('data/user.log', mode='rt', encoding='utf-8') as file:
#     file.seek(0, 2)
#     while 1:
#         res = file.readline()
#         if res:
#             print(res.strip())
#         time.sleep(0.2)

import time

with open('data/user.log', mode='rb') as file:
    file.seek(0, 2)
    while 1:
        res = file.readline()
        if res:
            print(res.strip().decode('utf-8'))
        time.sleep(0.2)
