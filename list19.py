# List19. Дан список из N строк. Вывести строки в порядке возрастания длины
# и отдельно самую длинную (max с key).
n = int(input())
s = []
for i in range(n):
    s.append(input())
print(sorted(s, key=len))
print(max(s, key=len))
