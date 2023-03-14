f = open('107_27_A.txt')
n = int(f.readline())
bins = [0] * n
for i in range(0, n):
    bins[i] = int(f.readline())
min_price = 2 ** 244
min_fact_pos = 0
prev = 0
for fact_pos in range(0, n):
    price = 0
    for bin_pos in range(0, n):
        dir_way = abs(bin_pos - fact_pos)
        short = min(dir_way, n - dir_way)
        price += short * bins[bin_pos]
    prev = price
    if price < min_price:
        min_price = price
print(min_price)
#https://inf-ege.sdamgia.ru/problem?id=45261