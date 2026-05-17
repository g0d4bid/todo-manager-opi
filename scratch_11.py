def shell_sort(b):
    n = len(b)
    a = n // 2
    while a > 0:
        for i in range(a, n):
            c = b[i]
            j = i
            while j >= a and b[j - a] > c:
                b[j] = b[j - a]
                j -= a
            b[j] = c
        a //= 2
    return b
b = list(map(int, input("числа через пробел: ").split()))
print(f"отсортировано: {shell_sort(b)}")