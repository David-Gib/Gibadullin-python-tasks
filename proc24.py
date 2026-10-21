# Proc24. Функция even(k) возвращает True для чётного k.
# Найти количество чётных чисел в наборе из 10 чисел.
def even(k):
    """Возвращает True, если k чётное, иначе False. Ничего не печатает."""
    return k % 2 == 0


count = 0
for i in range(10):
    k = int(input())
    if even(k):
        count += 1
print(count)
