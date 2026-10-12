# Err6. Та же задача, что Err5, но с двумя ветками:
# нечисловой индекс — "Ошибка ввода", индекс вне границ — "Нет такого символа".
word = input()
try:
    index = int(input())
    print(word[index])
except ValueError:
    print("Ошибка ввода")
except IndexError:
    print("Нет такого символа")
