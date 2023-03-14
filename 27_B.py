f = open('27-B.txt')
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
min_fact = 0
plus_sum = 0
minus_sum = 0
cnt = 0
while cnt < n // 2:
    minus_sum += bins[cnt]
    cnt += 1
while cnt < n:
    plus_sum += bins[cnt]
    cnt += 1
for fact_pos in range(1, n):
    plus_sum += bins[fact_pos - 1] - bins[fact_pos - 1 - n // 2]
    minus_sum += bins[fact_pos - 1 - n // 2] - bins[fact_pos - 1]
    base_price += plus_sum - minus_sum
    if base_price < min_price:
        min_price = base_price
        min_fact = fact_pos + 1
print(min_price, min_fact)