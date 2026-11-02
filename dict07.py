# Задание: Построить словарь из N пар. Вывести ключ с наибольшим значением (перебор с кандидатом; значения различны).

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
best = next(iter(d))
for key in d:
    if d[key] > d[best]:
        best = key
print(best)
