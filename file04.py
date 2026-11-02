# Задание: Даны имена четырёх файлов. Найти количество существующих среди них в текущем каталоге.

import os

count = 0
for i in range(4):
    name = input()
    if os.path.exists(name):
        count += 1
print(count)
