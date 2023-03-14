start = 1
end = 30
num = [0] * (end + 1)
num[start] = 1
for i in range(start, end):
    if i + 2 <= end and not (i < 14 < i + 2):
        num[i + 2] += num[i]
    if i * 2 <= end and not (i < 14 < i * 2):
        num[i * 2] += num[i]
print(num[end])