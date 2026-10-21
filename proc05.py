# Proc5. Функция rect_ps(x1, y1, x2, y2) возвращает периметр и площадь
# прямоугольника со сторонами, параллельными осям координат, по
# противоположным вершинам (x1, y1) и (x2, y2).
# Найти P и S для трёх прямоугольников.
def rect_ps(x1, y1, x2, y2):
    """Возвращает кортеж (P, S) прямоугольника по двум вершинам.

    Стороны — модули разностей координат. Ничего не печатает.
    """
    width = abs(x2 - x1)
    height = abs(y2 - y1)
    return 2 * (width + height), width * height


for i in range(3):
    x1 = float(input())
    y1 = float(input())
    x2 = float(input())
    y2 = float(input())
    p, s = rect_ps(x1, y1, x2, y2)
    print(p)
    print(s)
