# Задание: Построить словарь из N троек: название, цена, количество (значение — список из двух чисел). Вывести суммарную стоимость склада и название самого дорогого по стоимости предмета.

n = int(input())
d = {}
for i in range(n):
    name = input()
    price = int(input())
    qty = int(input())
    d[name] = [price, qty]
total = 0
best = next(iter(d))
for name in d:
    price, qty = d[name]
    total += price * qty
    best_price, best_qty = d[best]
    if price * qty > best_price * best_qty:
        best = name
print(total)
print(best)
