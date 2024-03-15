def digits(n, t):
    digit = 0
    for i1 in range(n):
        digit += 10 ** i1 * t
    return digit


N, T = map(int, input().split())
sum1 = 0
for i in range(1, N + 1):
    sum1 += digits(i, T)
print(int(sum1), end=" ")
