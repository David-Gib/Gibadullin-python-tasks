#Даны два ненулевых числа. Найти сумму, разность, произведение и частное их модулей.
a = float(input())
b = float(input())
if a and b != 0:
    x = abs(a)
    y = abs(b)
    print(x + y, x - y, x * y, x / y)