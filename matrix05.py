# Задание: Даны M, N, число D и набор из M чисел. Первый столбец — набор; каждый следующий столбец равен предыдущему плюс D по строкам.

m = int(input())
n = int(input())
d = int(input())
values = [int(x) for x in input().split()]
a = []
for i in range(m):
    row = []
    for j in range(n):
        row.append(values[i] + d * j)
    a.append(row)
for row in a:
    print(row)
