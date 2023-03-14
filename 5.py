cnt = 0
for i1 in range(1,10,2):
    for i2 in range(1, 10,2):
        for i3 in range(1, 10,2):
            for i4 in range(1, 10,2):
                a = i1 + i3
                b = i2 + i4
                if (a == 4 or b == 4) and (a == 14 or b == 14):
                    cnt+=1
print(cnt)