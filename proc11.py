# Proc11. Функция minmax(x, y) возвращает пару (меньшее, большее).
# Четырьмя вызовами найти минимум и максимум четырёх данных чисел
# A, B, C, D. Вывести сначала минимум, затем максимум.
def minmax(x, y):
    """Возвращает кортеж (меньшее, большее). Ничего не печатает."""
    if x < y:
        return x, y
    return y, x


a = float(input())
b = float(input())
c = float(input())
d = float(input())
# сначала упорядочиваем пары (A, B) и (C, D)
a, b = minmax(a, b)
c, d = minmax(c, d)
# меньшие между собой дадут минимум, большие между собой — максимум
minimum, other = minmax(a, c)
other, maximum = minmax(b, d)
print(minimum)
print(maximum)
