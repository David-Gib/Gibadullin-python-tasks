# List26. Дан список A из N чисел. Генератором вывести элементы, большие
# среднего, и само среднее.
# Среднее считаем до генератора, чтобы оно не пересчитывалось на каждом элементе.
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
average = sum(a) / len(a)
big = [x for x in a if x > average]
print(big)
print(f"{average:.1f}")
