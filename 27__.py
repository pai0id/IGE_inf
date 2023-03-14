f = open("27_B.txt")
n = int(f.readline())
mn_ostat = [0] + [2 ** 32] * 43
mn_len = [0] + [2 ** 32] * 43
ans = []
summa = 0
for i in range(1, n + 1):
    x = int(f.readline())
    summa += x
    if mn_ostat[summa % 43] != 2 ** 32:
        ans.append((summa - mn_ostat[summa % 43], -(i - mn_len[summa % 43])))
    else:
        mn_ostat[summa % 43] = summa
        mn_len[summa % 43] = i
print(max(ans))
