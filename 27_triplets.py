f = open("27_B.txt")
min_delt = 2 ** 34
n = f.readline()
s = 0
for line in f:
    a, b, c = line.split()
    a = int(a)
    b = int(b)
    c = int(c)
    m = max(a, b, c)
    s += m
    for i in (a, b, c):
        i = int(i)
        if m % 109 != i % 109:
            min_delt = min(min_delt, m - i)
if s % 109 != 0:
    print(s)
else:
    print(s - min_delt)
