arr = input()
num = [int(n) for n in arr.split()]
txt = int(input())
for i in range(len(num) - 1):
    for j in range(i + 1, len(num)):
        if num[i] + num[j] == txt:
            print(f"{i} {j}")
            break
