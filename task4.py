# Требуется определить, можно ли от шоколадки размером n × m долек отломить k долек,
# если разрешается сделать один разлом по прямой между дольками
# (то есть разломить шоколадку на два прямоугольника).
# Пример:
# 3 2 4 -> yes
# 3 2 1 -> no

x = int(input('высота долек: '))
y = int(input('ширина долек: '))
k = int(input('на сколько хотите поделить шоколад ?: '))
xy = x * y
if xy % k > 0:
    print('yes')
else:
    print('no')