# List28. Дан список из N строк и буква. Генератором вывести строки,
# начинающиеся с этой буквы (первый символ строки).
# Сначала читаем N и строки, буква идёт после списка.
n = int(input())
words = []
for i in range(n):
    words.append(input())
letter = input()
result = [s for s in words if s[0] == letter]
print(result)
