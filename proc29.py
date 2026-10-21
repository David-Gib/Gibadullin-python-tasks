# Proc29. Функция digit_count(k) возвращает количество цифр числа k (> 0).
# Найти количество цифр пяти данных чисел.
def digit_count_sum(k):
    """Возвращает кортеж (количество цифр, сумма цифр) числа k > 0.

    Перенесена из Proc6. Ничего не печатает.
    """
    count = 0
    total = 0
    while k > 0:
        total += k % 10
        count += 1
        k //= 10
    return count, total


def digit_count(k):
    """Возвращает количество цифр числа k > 0. Ничего не печатает."""
    count, total = digit_count_sum(k)
    return count


for i in range(5):
    k = int(input())
    print(digit_count(k))
