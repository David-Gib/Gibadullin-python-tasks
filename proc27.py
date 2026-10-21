# Proc27. Функция is_power_n(k, n) возвращает True, если k (> 0) — степень
# числа n (> 1). Даны n и набор из 10 чисел: найти количество степеней.
def is_power_n(k, n):
    """Возвращает True, если k > 0 — степень числа n > 1. Ничего не печатает.

    Делим на n, пока делится без остатка; единица в конце — степень.
    """
    rest = k
    while rest % n == 0:
        rest //= n
    return rest == 1


n = int(input())
count = 0
for i in range(10):
    k = int(input())
    if is_power_n(k, n):
        count += 1
print(count)
