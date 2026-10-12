# For3. Даны два целых числа A и B (A < B). Вывести в порядке убывания
# все целые числа, расположенные между A и B (не включая сами числа A и B),
# а также количество N этих чисел.
a = int(input())
b = int(input())
count = 0
for i in range(b - 1, a, -1):
    print(i)
    count += 1
print(count)
