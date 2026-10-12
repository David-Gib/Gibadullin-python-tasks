# While11 с защитой. Дано N (> 1). Вывести наименьшее K, при котором
# сумма 1 + 2 + ... + K >= N, и саму сумму.
# При нечисловом вводе вывести "Ошибка ввода". Защищено только чтение N,
# цикл стоит в else и не меняется.
try:
    n = int(input())
except ValueError:
    print("Ошибка ввода")
else:
    total = 0
    k = 0
    while total < n:
        k += 1
        total += k
    print(k)
    print(total)
