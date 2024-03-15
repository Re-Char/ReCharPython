x = int(input())
arr = input()
num = [int(n) for n in arr.split()]
statics = [0] * 10
for i in range(x):
    if num[i] <= 9:
        statics[0] += 1
    elif 9 < num[i] <= 19:
        statics[1] += 1
    elif 19 < num[i] <= 29:
        statics[2] += 1
    elif 29 < num[i] <= 39:
        statics[3] += 1
    elif 39 < num[i] <= 49:
        statics[4] += 1
    elif 49 < num[i] <= 59:
        statics[5] += 1
    elif 59 < num[i] <= 69:
        statics[6] += 1
    elif 69 < num[i] <= 79:
        statics[7] += 1
    elif 79 < num[i] <= 89:
        statics[8] += 1
    elif 89 < num[i] <= 100:
        statics[9] += 1
for i in range(9):
    print(statics[i], end=',')
print(statics[9])
for i in range(10):
    if i < 9:
        print("%2d" % (i * 10) + " - " + "%2d" % ((i + 1) * 10 - 1) + ':', end='')
    else:
        print("%2d" % (i * 10) + " -" + "%2d" % ((i + 1) * 10) + ':', end='')
    for j in range(statics[i]):
        print('*', end='')
    print()
