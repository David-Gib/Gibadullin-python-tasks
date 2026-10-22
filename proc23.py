# Proc23. Функция quarter(x, y) возвращает номер координатной четверти
# точки с ненулевыми координатами. Найти четверти трёх точек.
def quarter(x, y):
    if x > 0 and y > 0:
        return 1
    elif x < 0 and y > 0:
        return 2
    elif x < 0 and y < 0:
        return 3
    else:
        return 4


for i in range(3):
    x = float(input())
    y = float(input())
    print(quarter(x, y))
