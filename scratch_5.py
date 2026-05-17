import random
a = 5
b = []
for i in range(a):
    b.append(random.randint(1,100))
print('не сортированные числа',b)
b.sort()
print('сортированные числа',b)