# Задание: Построить словарь из N пар с различными значениями. Построить обращённый словарь: значение — ключ. Вывести его пары в порядке добавления исходного.

n = int(input())
d = {}
for i in range(n):
    key = input()
    value = int(input())
    d[key] = value
reverse = {}
for key, value in d.items():
    reverse[value] = key
for value, key in reverse.items():
    print(f"{value}: {key}")
