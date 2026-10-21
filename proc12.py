# Proc12. Описать функцию sort_inc3(a, b, c), возвращающую три значения,
# упорядоченные по возрастанию. Упорядочить два данных набора из трёх чисел.
def sort_inc3(a, b, c):
    """Возвращает кортеж (a, b, c), упорядоченный по возрастанию.

    Три попарных обмена. Ничего не печатает.
    """
    if a > b:
        a, b = b, a
    if b > c:
        b, c = c, b
    if a > b:
        a, b = b, a
    return a, b, c


a1 = float(input())
b1 = float(input())
c1 = float(input())
a2 = float(input())
b2 = float(input())
c2 = float(input())
x, y, z = sort_inc3(a1, b1, c1)
print(x)
print(y)
print(z)
x, y, z = sort_inc3(a2, b2, c2)
print(x)
print(y)
print(z)
