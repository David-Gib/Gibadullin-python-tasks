# Proc13. Описать функцию sort_dec3(a, b, c), возвращающую три значения,
# упорядоченные по убыванию. Упорядочить два данных набора из трёх чисел.
def sort_dec3(a, b, c):
    """Возвращает кортеж (a, b, c), упорядоченный по убыванию.

    Зеркало sort_inc3: те же три обмена, но по знаку «меньше».
    Ничего не печатает.
    """
    if a < b:
        a, b = b, a
    if b < c:
        b, c = c, b
    if a < b:
        a, b = b, a
    return a, b, c


a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
x, y, z = sort_dec3(a1, b1, c1)
print(x)
print(y)
print(z)
x, y, z = sort_dec3(a2, b2, c2)
print(x)
print(y)
print(z)
