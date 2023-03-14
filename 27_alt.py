f = open('107_27_A.txt')
n = int(f.readline())
bins = [0] * n
for i in range(0, n):
    bins[i] = int(f.readline())
base_price = 0
for base_bin_pos in range(0, n):
    dir_way = base_bin_pos
    short = min(dir_way, n - dir_way)
    base_price += short * bins[base_bin_pos]
min_price = base_price
min_bin = 0
for fact_pos in range(1, n):
    cnt = 1
    while cnt <= n // 2:
        if fact_pos > n - 1:
            fact_pos -= n
        base_price -= bins[fact_pos]
        fact_pos += 1
        cnt += 1
    while cnt <= n:
        if fact_pos > n - 1:
            fact_pos -= n
        base_price += bins[fact_pos]
        fact_pos += 1
        cnt += 1
    if base_price < min_price:
        min_price = base_price
        min_bin = fact_pos + 1
print(min_price, min_bin)
