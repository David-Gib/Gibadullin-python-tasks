# Задание: Дано имя файла и вещественные A и D. Записать в файл 10 первых членов прогрессии A, A+D, A+2·D, …

name = input()
a = float(input())
d = float(input())
with open(name, "w", encoding="utf-8") as f:
    for i in range(10):
        f.write(str(a + i * d) + "\n")
