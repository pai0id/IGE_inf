f = open("24_2.txt")
l = f.readline()
f.close()
cnt = 0
maxi = 0
i = 0
while i < len(l):
    if (l[i] == "A" or l[i] == "C") and l[i + 1] == "B":
        i += 2
        cnt += 1
    else:
        maxi = max(cnt, maxi)
        cnt = 0
        i += 1
print(maxi)
