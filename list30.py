# List30. Дан список из N строк. Генератором вывести список длин строк
# и суммарную длину всех строк.
n = int(input())
words = []
for i in range(n):
    words.append(input())
lengths = [len(s) for s in words]
print(lengths)
print(sum(lengths))
