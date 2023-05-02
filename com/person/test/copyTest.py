# 深拷贝的引用
import copy

# 浅拷贝
# copy 方法
l1 = ['张大仙', '徐凤年', ['李淳罡', '邓太阿']]
l2 = l1
l3 = l1.copy()

print(id(l1), id(l2), id(l3))
print(id(l1[0]), id(l2[0]), id(l3[0]))
print(id(l1[1]), id(l2[1]), id(l3[1]))
print(id(l1[2]), id(l2[2]), id(l3[2]))

l1[0] = '张坦克'
print(id(l1[0]), id(l2[0]), id(l3[0]))
print(l1[0], l2[0], l3[0])

# 不可变变量的值就不会变，所有值都改变
l1[2][0] = '李大嘴'
print(id(l1[2]), id(l2[2]), id(l3[2]))
print(l1[2][0], l2[2][0], l3[2][0])

# 深拷贝

l4 = copy.deepcopy(l1)
print(id(l4[2]), id(l1[2]))
