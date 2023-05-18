# coding: utf-8
# @Author: Sheamus

def login():
    print("登录功能")


def register():
    print("注册功能")


def pay():
    print("扫码支付")


def cashin():
    print("充值功能")


def transfer():
    print("转账功能")


def withdraw():
    print("提现功能")


funcDicts = {
    "0": (None, "退出"),
    "1": (register, "注册"),
    "2": (login, "登录"),
    "3": (pay, "支付"),
    "4": (cashin, "充值"),
    "5": (transfer, "转账"),
    "6": (withdraw, "提现")
}

while True:
    print("功能列表：")
    for opt in funcDicts:
        print("输入 ", opt, " ", funcDicts[opt][1])

    print("请输入你要的功能：")
    req = input()

    if req not in funcDicts:
        print("输入错误。。。")
        continue
    if req == "0":
        print("退出程序。。。")
        break
    funcDicts[req][0]()
