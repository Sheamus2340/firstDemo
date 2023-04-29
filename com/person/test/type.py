name = "张大仙"
name2 = "坦克"

name2 = name + "是" + name2
print(name2)

name = name * 5
print(name)

print("-" * 20)

info = [0, '张大仙', 18, '坦克']
print(type(info))
print(info[1], info[-1])

person = {
    "name": "张大仙",
    "age": 18
}

print(type(person))
print(person)
print(person.get("name"))

is_sleep = True
print(type(is_sleep))
print(is_sleep)


name = input("请输入名称：")
print(name, type(name))

if 10:
    print('True')
