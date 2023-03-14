f = open("24_1.txt", "r")
l = f.read()
i = 0
cnt = 0
maxim = 0
d_cnt = 0
d_pos = 0
while i < len(l):
    if l[i] != "D":
        cnt += 1
    else:
        d_cnt += 1
        if d_cnt == 1:
            d_pos = i
            cnt += 1
        if d_cnt > 1:
            maxim = max(cnt, maxim)
            cnt = 0
            d_cnt = 0
            i = d_pos
    i += 1
print(maxim)
f.close()
