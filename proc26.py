# Proc26. Функция is_power5(k) возвращает True, если k (> 0) — степень
# пятёрки. Найти количество таких чисел в наборе из 10 чисел.
def is_power5(k):
    """Возвращает True, если k > 0 — степень числа 5. Ничего не печатает.

    Делим на 5, пока делится без остатка; единица в конце — степень.
    """
    rest = k
    while rest % 5 == 0:
        rest //= 5
    return rest == 1


count = 0
for i in range(10):
    k = int(input())
    if is_power5(k):
        count += 1
print(count)
