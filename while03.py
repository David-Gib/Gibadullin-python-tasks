# While3. Даны целые положительные числа N и K. Используя только операции
# сложения и вычитания, найти частное от деления нацело N на K,
# а также остаток от этого деления.
n = int(input())
k = int(input())
quotient = 0
rest = n
while rest >= k:
    rest -= k
    quotient += 1
print(quotient)
print(rest)
