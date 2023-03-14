list = []
f = open('28129_B.txt')
for line in f:
    line = line.replace('\n','')
    list.append(line)
del list[0]
f.close()
maxa = 0
maxb = 0
max = 0
for a in list:
    a = int(a)
    for b in list:
        b = int(b)
        if (((a%160) != (b%160)) and ((a%7 == 0) or (b%7 == 0))) and max<(a+b) and (a != b):
            max = a+b
            maxa = a
            maxb = b
print(maxa,' ', maxb)
#https://inf-ege.sdamgia.ru/problem?id=28129