names = ['张大仙', '张宏发', '张坦克']
for a in names:
    print(a)

person = {'name': '张大仙', 'age': 18, 'score': 100}
for per in person:
    print(per, '是', person[per])

for i in range(10):
    print(i)

for i in range(1, 10):
    for j in range(1, i + 1):
        print(f'{i} * {j} = {i * j}', end='\t\t')
    print('\n')
