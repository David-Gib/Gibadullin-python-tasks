# Задание: Даны M, N и набор из M чисел. Сформировать матрицу, у которой в каждом столбце содержатся все числа набора в том же порядке.

m = int(input())
n = int(input())
values = [int(x) for x in input().split()]
a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(values[i])
    a.append(row)
for row in a:
    print(row)
