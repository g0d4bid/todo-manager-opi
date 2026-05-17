import random
a = 10
b = 5
c = [random.randint(1,100) for _ in range(a)]
print(f'Числа: {c}')
d = 0
for element in c:
    if element % b == 0:
        d += 1
print(f'Количество чисел, кратных {b}: {d}')