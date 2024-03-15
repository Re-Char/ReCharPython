def change(n, m):
    num1_list = {}
    count1 = 0
    while n != 0:
        num1_list[count1] = n % 10
        n = int(n / 10)
        count1 += 1
    rr = 0
    for i1 in range(count1):
        rr += num1_list[count1 - 1 - i1] * (m ** (count1 - 1 - i1))
    return rr


def judge(n, m):
    num2_list = {}
    count2 = 0
    while n != 0:
        num2_list[count2] = n % 10
        n = int(n / 10)
        count2 += 1
    for i2 in range(count2):
        if num2_list[i2] >= m:
            return 0
    return 1


a, b, result = map(int, input().split())
point = 0
for i in range(2, 100):
    if change(a, i) * change(b, i) == change(result, i):
        if judge(a, i) and judge(b, i) and judge(result, i):
            point = 1
            print(i)
            break
        else:
            point = 0
if point == 0:
    print(0)
