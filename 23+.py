start = 2
end = 22
num = [0] * (end + 1)
num[start] = 1
for i in range(start, end):
    if i == 25:
        continue
    if i + 1 <= end and not (i < 14 < i + 1):
        num[i + 1] += num[i]
print(num[end])
