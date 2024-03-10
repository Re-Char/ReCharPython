from sys import argv

script, str1 = argv
b = list(str1)
for i in range(len(b)):
    for j in range(i, len(b)):
        if b[i].isupper() and b[j].islower():
            if ord(b[i]) + 32 > ord(b[j]):
                b[i], b[j] = b[j], b[i]
            else:
                continue
        elif b[i].islower() and b[j].isupper():
            if ord(b[i]) - 32 > ord(b[j]):
                b[i], b[j] = b[j], b[i]
            else:
                continue
        elif b[i].isalpha() and b[j].isalpha():
            if b[i] > b[j]:
                b[i], b[j] = b[j], b[i]
            else:
                continue
str1 = ''.join(b)
print(str1)
