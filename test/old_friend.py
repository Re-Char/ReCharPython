arr = input()
num = [int(n) for n in arr.split()]
num2 = [int(n) for n in arr.split()]
hash_list = [0] * len(num)
for i in range(len(num)):
    for j in range(len(num2)):
        if num[i] == num2[j]:
            hash_list[i] += 1
    if hash_list[i] == 1:
        print(num[i])
        break
