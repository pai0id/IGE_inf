st =102
end = 5
num = [0]*(st+1)
num[st] = 1
for i in range(st,end,-1):
    if i - 8 >= end and not(i>43>i-8):
        num[i-8]+=num[i]
    if i //2 >= end and not(i>43>i//2):
        num[i//2]+=num[i]
print(num[end])