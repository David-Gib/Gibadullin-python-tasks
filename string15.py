# Задание: Дана строка. Подсчитать общее количество строчных латинских и русских букв в ней.

s = input()
alphabet = "abcdefghijklmnopqrstuvwxyzабвгдежзийклмнопрстуфхцчшщъыьэюяё"
count = 0
for ch in s:
    if ch in alphabet:
        count += 1
print(count)
