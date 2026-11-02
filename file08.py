# Задание: Даны имена двух файлов: первый существует и непуст, второй отсутствует. Создать второй и записать в него первый и последний элементы первого.

src = input()
dst = input()
with open(src, encoding="utf-8") as f:
    first = f.readline().strip()
    last = first
    for line in f:
        if line.strip() != "":
            last = line.strip()
with open(dst, "w", encoding="utf-8") as f:
    f.write(first + "\n")
    f.write(last + "\n")
