# Задание: Дана строка S. Если S — допустимое имя файла, создать пустой файл с этим именем и вывести True, иначе False.

name = input()
try:
    with open(name, "w", encoding="utf-8") as f:
        pass
    print(True)
except OSError:
    print(False)
