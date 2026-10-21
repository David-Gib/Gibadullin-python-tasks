# Proc18. Функция circle_s(r) возвращает площадь круга радиуса r (π = 3.14).
# Найти площади трёх кругов.
def circle_s(r):
    """Возвращает площадь круга S = 3.14·r². Ничего не печатает."""
    return 3.14 * r * r


for i in range(3):
    r = float(input())
    print(circle_s(r))
