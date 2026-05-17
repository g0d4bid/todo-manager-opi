import random
a = 5
b = []
for i in range(a):
    b.append(random.randint(1,100))
print(f'не сортированные числа: {b}')
b.sort()
print(f'сортированные числа: {b}')
print(f'медиана: {b[2]}')