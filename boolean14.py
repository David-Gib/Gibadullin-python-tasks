# Boolean14. Даны три целых числа: A, B, C. Проверить истинность высказывания:
# «Ровно одно из чисел A, B, C положительное».
a = int(input())
b = int(input())
c = int(input())
count = (a > 0) + (b > 0) + (c > 0)
print(count == 1)
