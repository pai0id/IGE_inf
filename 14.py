for n in range(2, 200):
    l = ""
    f = 144
    while f > 0:
        l = l + str(f % n)
        f = f // n
    print(l)
    print(n)
