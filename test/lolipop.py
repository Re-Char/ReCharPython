yuan, jiao = map(int, input().split())
Y = 10 * yuan + jiao
t = Y % 67
Y -= t
count = 0
while Y != 0:
    if Y > 100:
        digit = int(Y / 100)
        Y -= digit * 67
    else:
        digit = 1
        Y -= 67
    count += digit
print(count)
