a = input("введите числа через пробел: ").split()
print(f"было: {a}")
n = len(a)
for i in range(n):
    for j in range(n - 1):
        if a[j] > a[j + 1]:
            a[j], a[j + 1] = a[j + 1], a[j]
print(f"стало: {a}")