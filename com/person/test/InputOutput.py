# 输入输出
"""
输出：
1. %占位符
    占位符：
    s: 字符串
    d: 有符号十进制整数和i一样
    c: 字符
    i：有符号十进制整数
    u：无符号十进制整数
    o: 八进制整数
    x: 16进制整数（小写字母）
    e：索引符号（小写e）
    E：索引符号（大写E）
    f：浮点实数
    g：f和e的简写
    G: f和E的简写
2. {} + format()
    name = "张三"
    print("你好{}".format(name))
"""

name = "张三"
classPro = "清华大学"
age = 21

print("大家好，我叫%s，来自%s，今年%d岁" % (name, classPro, age))

name = "张三"
print("你好{}".format(name))

"""
输入：
1. 接收键盘的输入： input() 方法
   注意：返回结果都是字符串，如果是数字就只能做强制转换
"""

name = input("请输入姓名：")
age = int(input("请输入年龄："))
print("你好，我叫%s, 今年%d" % (name, age))
