# Proc15. Функция shift_left3(a, b, c) возвращает тройку после левого
# циклического сдвига: a переходит на место c, c — на место b, b — на
# место a. Сдвинуть два данных набора из трёх чисел.
def shift_left3(a, b, c):
    """Возвращает тройку после левого циклического сдвига.

    На месте a окажется старое b, на месте b — старое c,
    на месте c — старое a. Ничего не печатает.
    """
    return b, c, a


a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
a1, b1, c1 = shift_left3(a1, b1, c1)
print(a1)
print(b1)
print(c1)
a2, b2, c2 = shift_left3(a2, b2, c2)
print(a2)
print(b2)
print(c2)
