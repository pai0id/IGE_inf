f = open('24-179.txt', 'r')
l = ''
for line in f:
    l += line
f.close()
norm = False
c_cnt = 0
d_cnt = 0
e_cnt = 0
for i in range(0, len(l) - 5):
    if l[i] == 'C' and l[i+1] == "B" and (l[i+2] == "C" or l[i+2] == "D" or l[i+2] == "E") and l[i+3] == "B" and l[i+4] == "C":
        if l[i+2] == "C":
            c_cnt+=1
        if l[i+2] == "D":
            d_cnt+=1
        if l[i+2] == "E":
            e_cnt+=1
print("C =", c_cnt, "D =", d_cnt, "E=", e_cnt)
print(c_cnt+d_cnt+e_cnt)