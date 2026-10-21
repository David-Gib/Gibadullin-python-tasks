# Proc16. Описать функцию sign(x), возвращающую -1 при x < 0, 0 при x = 0
# и 1 при x > 0. Найти значение выражения Sign(A) + Sign(B) для данных A и B.
def sign(x):
    """Возвращает -1, 0 или 1 по знаку x. Ничего не печатает."""
    if x < 0:
        return -1
    if x == 0:
        return 0
    return 1


a = float(input())
b = float(input())
print(sign(a) + sign(b))
