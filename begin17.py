#Даны три точки A, B, C на числовой оси. Найти длины отрезков AC и BC и их сумму.
A = float(input())
B = float(input())
C = float(input())

AC = A + C
BC = B + C
ACBC = AC + BC
print(AC, BC, ACBC)