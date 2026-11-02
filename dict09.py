# Задание: Построить словари из N и M пар. Слить второй в первый через update. Вывести размер результата и значение ключа, который был в обоих словарях (такой ключ гарантированно есть).

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
k = input()
d.update(other)
print(len(d))
print(d[k])
