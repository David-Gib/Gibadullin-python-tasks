#Даны три точки A, B, C на числовой оси. Точка C расположена между точками A и B. Найти произведение длин отрезков AC и BC.
# Ввод координат точек A, B, C
a = float(input())
b = float(input())
c = float(input())

ac = abs(c - a)
bc = abs(b - c)
product = ac * bc

print(ac)
print(bc)
print(product)