# Proc9. Функция add_left_digit(d, k) возвращает число k с приписанной
# слева цифрой d (1–9). Приписать к данному K слева D1 и D2, печатая
# результат каждого шага.
def digit_count_sum(k):
    """Возвращает кортеж (количество цифр, сумма цифр) числа k > 0."""
    count = 0
    total = 0
    while k > 0:
        total += k % 10
        count += 1
        k //= 10
    return count, total


def add_left_digit(d, k):
    """Возвращает число k с приписанной слева цифрой d. Ничего не печатает.

    Слева d умножается на десять в степени «число цифр k».
    """
    count, total = digit_count_sum(k)
    return d * 10 ** count + k


k = int(input())
d1 = int(input())
d2 = int(input())
k = add_left_digit(d1, k)
print(k)
k = add_left_digit(d2, k)
print(k)
