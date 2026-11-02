# Задание: Даны имена двух файлов: один существует и непуст (не обязательно первый), другой отсутствует. Создать отсутствующий и записать в него конечный и начальный элементы существующего.

import os

name1 = input()
name2 = input()
if os.path.exists(name1):
    src = name1
    dst = name2
else:
    src = name2
    dst = name1
with open(src, encoding="utf-8") as f:
    first = f.readline().strip()
    last = first
    for line in f:
        if line.strip() != "":
            last = line.strip()
with open(dst, "w", encoding="utf-8") as f:
    f.write(last + "\n")
    f.write(first + "\n")
