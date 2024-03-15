import math


def prime(x):
    for i1 in range(2, int(math.sqrt(x)) + 1):
        if x % i1 == 0:
            return 0
    return 1


def reverse(x):
    re_x = 0
    digit_list = {}
    i2 = 0
    while x > 0:
        digit_list[i2] = x % 10
        i2 += 1
        x = int(x / 10)
    for j in range(i2):
        re_x += 10 ** (i2 - j - 1) * digit_list[j]
    return re_x


n = int(input())
count = 0
for i in range(2, n + 1):
    re_i = reverse(i)
    if prime(i) and prime(re_i):
        count += 1
print(count)
