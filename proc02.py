# Proc2. Функция power_a234(a) возвращает вторую, третью и четвёртую
# степени числа a. Найти три степени пяти данных чисел.
def power_a234(a):
    """Возвращает кортеж (a**2, a**3, a**4). Ничего не печатает."""
    return a ** 2, a ** 3, a ** 4


for i in range(5):
    a = float(input())
    second, third, fourth = power_a234(a)
    print(second)
    print(third)
    print(fourth)
