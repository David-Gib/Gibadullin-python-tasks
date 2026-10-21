# Proc17. Функция roots_count(a, b, c) возвращает число корней квадратного
# уравнения по дискриминанту D = b² − 4·a·c (a ≠ 0).
# Найти количество корней трёх уравнений.
def roots_count(a, b, c):
    """Возвращает 0, 1 или 2 — число корней уравнения a·x² + b·x + c = 0.

    D вещественный, поэтому с нулём сравнивается через abs(D) < 1e-9.
    Ничего не печатает.
    """
    d = b * b - 4 * a * c
    if abs(d) < 1e-9:
        return 1
    if d > 0:
        return 2
    return 0


for i in range(3):
    a = float(input())
    b = float(input())
    c = float(input())
    print(roots_count(a, b, c))
