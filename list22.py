# List22. Дан список A из N чисел и число D. Генератором вывести элементы,
# умноженные на D, и количество элементов, равных D.
# Сначала читаем N и элементы, число D идёт после списка.
n = int(input())
a = []
for i in range(n):
    a.append(int(input()))
d = int(input())
multiplied = [x * d for x in a]
equal = [x for x in a if x == d]
print(multiplied)
print(len(equal))
