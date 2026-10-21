# Proc10. Описать функцию swap(x, y), возвращающую пару значений в обратном
# порядке. Для данных A, B, C, D поменять содержимое пар A и B, C и D,
# B и C и вывести новые значения A, B, C, D.
def swap(x, y):
    """Возвращает пару (y, x). Переменные вызвавшего не меняет."""
    return y, x


a = float(input())
b = float(input())
c = float(input())
d = float(input())
a, b = swap(a, b)
c, d = swap(c, d)
b, c = swap(b, c)
print(a)
print(b)
print(c)
print(d)
