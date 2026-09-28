#Найти расстояние между двумя точками с заданными координатами (x1, y1) и (x2, y2) на плоскости. Расстояние вычисляется по формуле √((x2 − x1)2 + (y2 − y1)2).
x1 = float(input("Введите x1:"))
y1 = float(input("Введите y1:"))
x2 = float(input("Введите x2:"))
y2 = float(input("Введите y2:"))

dx = x2 - x1
dy = y2 - y1

dx_sq = dx * dx
dy_sq = dy * dy
sum_sq = dx_sq + dy_sq
distance = sum_sq ** 0.5

print( distance)