# Задание: Построить словари из N и M пар. Добавить в первый пары второго без update: только ключи, которых нет; совпавшие ключи считать проигнорированными. Вывести размер и число проигнорированных.

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
m = int(input())
other = {}
for i in range(m):
    key = input()
    value = int(input())
    other[key] = value
ignored = 0
for key, value in other.items():
    if key in d:
        ignored += 1
    else:
        d[key] = value
print(len(d))
print(ignored)
