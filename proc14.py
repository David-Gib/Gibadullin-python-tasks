# Proc14. Функция shift_right3(a, b, c) возвращает тройку после правого
# циклического сдвига: a переходит на место b, b — на место c, c — на
# место a. Сдвинуть два данных набора из трёх чисел.
def shift_right3(a, b, c):
    """Возвращает тройку после правого циклического сдвига.

    На месте a окажется старое c, на месте b — старое a,
    на месте c — старое b. Ничего не печатает.
    """
    return c, a, b


a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
a1, b1, c1 = shift_right3(a1, b1, c1)
print(a1)
print(b1)
print(c1)
a2, b2, c2 = shift_right3(a2, b2, c2)
print(a2)
print(b2)
print(c2)
