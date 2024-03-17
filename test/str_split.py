y = 'a2b3c4d7e1f6g5h8i9j0'
a = y[::2]
b = y[::-2]
c = list(b)
Sum = 0
for i in range(len(c)):
    for j in range(i, len(c)):
        if c[i] > c[j]:
            c[i], c[j] = c[j], c[i]
b = ''.join(c)
print(f"{b} {a}")
for i in range(len(c)):
    Sum += int(c[i])
print(Sum)
