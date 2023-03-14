l = "GEORIY"
cnt = 0
for i1 in l:
    for i2 in l:
        for i3 in l:
            for i4 in l:
                for i5 in l:
                    for i6 in l:
                        for i7 in l:
                            s = i1 + i2 + i3 + i4 + i5 + i6 + i7
                            if ("GG" in s) or s.count("G") > 2 or s.count("E") > 1 or s.count("O") > 1 or s.count(
                                    "R") > 1 or s.count("I") > 1 or s.count("Y") > 1:
                                continue
                            else:
                                cnt += 1
print(cnt)
#https://inf-ege.sdamgia.ru/problem?id=40983