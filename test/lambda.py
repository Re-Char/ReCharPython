from functools import reduce
double_func = lambda s: s * 2
num = map(int, input().split(" "))
print(list(map(double_func, num)))
plus = lambda x, y: x + y
num1 = map(int, input().split(" "))
num2 = map(int, input().split(" "))
print(list(map(plus, num1, num2)))
num3 = map(int, input().split(" "))
init = int(input())
print(reduce(plus, num3, init))
mode_2 = lambda x: x % 2
num4 = map(int, input().split(" "))
print(list(filter(mode_2, num4)))
pr = lambda x: x
print_num = lambda x: pr("one") if x == 1 else(pr("two") if x == 2 else pr("others"))
num_in = int(input())
print_num(num_in)
