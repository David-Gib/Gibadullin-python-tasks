# Задание: Даны непустая строка S и N (> 0). Вывести строку из символов S, между которыми вставлено по N звёздочек.

s = input()
n = int(input())
separator = "*" * n
print(separator.join(s))
