def dell(x):
    root = int(x ** 0.5)
    if root ** 2 == x:
        for d in range(2, root):
            if x % d == 0:
                d2 = x // d
                g = d2 - d
                return g
        return 0
    else:
        for d in range(2, root + 1):
            if x % d == 0:
                d2 = x // d
                g = d2 - d
                return g
        return 0


cnt = 1
for i in range(500000, 1000000):
    dd = dell(i)
    if dd != 0 and dd % 8 == 0:
        print(i, dd)
        cnt += 1
    if cnt > 7:
        break
