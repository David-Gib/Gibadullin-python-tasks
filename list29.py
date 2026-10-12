# List29. Дан список A из N чисел и число K. Вывести K наибольших элементов
# в порядке убывания (сортировка плюс срез).
# Сначала читаем N и элементы, число K идёт после списка.
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
k = int(input())
top = sorted(a, reverse=True)[:k]
print(top)
