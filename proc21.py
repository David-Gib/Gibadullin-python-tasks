# Proc21. Функция sum_range(a, b) возвращает сумму целых чисел от a до b
# включительно; если a > b, возвращает 0. Найти суммы от A до B и от B до C.
def sum_range(a, b):
    """Возвращает сумму целых от a до b включительно, а при a > b — 0.

    Ничего не печатает.
    """
    if a > b:
        return 0
    total = 0
    for i in range(a, b + 1):
        total += i
    return total


a = int(input())
b = int(input())
c = int(input())
print(sum_range(a, b))
print(sum_range(b, c))
