arr = input()
num = [int(n) for n in arr.split(' ')]
result = 0
for i in range(len(num) - 1):
    for j in range(i + 1, len(num)):
        if num[j] - num[i] > result:
            result = num[j] - num[i]
if result == 0:
    print(-1)
else:
    print(result)
