def lsd(a):
    m = max(a)
    e = 1
    while m // e > 0:
        b = [[] for _ in range(10)]
        for x in a:
            b[(x // e) % 10].append(x)
        a = [x for bkt in b for x in bkt]
        e *= 10
    return a
a = list(map(int, input().split()))
print(lsd(a))