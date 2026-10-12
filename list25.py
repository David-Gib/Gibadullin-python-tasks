# List25. Дан список A из N различных чисел. Вывести второй по величине элемент.
# Сортируем по убыванию, второй по величине — элемент с индексом 1.
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
ordered = sorted(a, reverse=True)
print(ordered[1])
