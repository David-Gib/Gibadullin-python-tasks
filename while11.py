# While11. Дано целое число N (> 1). Вывести наименьшее из целых чисел K,
# для которых сумма 1 + 2 + ... + K будет больше или равна N,
# и саму эту сумму.
n = int(input())
total = 0
k = 0
while total < n:
    k += 1
    total += k
print(k)
print(total)
