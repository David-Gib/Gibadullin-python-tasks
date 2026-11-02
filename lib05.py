# Задание: Lib5. По документации colorama выписать в комментарий три цвета Fore и две константы Style, не использованные в классе; одним из них покрасить строку победы над врагом. Проверка: цвет виден в терминале и не ломает вывод без colorama.

# Дополнительные цвета Fore: BLUE, CYAN, MAGENTA.
# Дополнительные константы Style: BRIGHT, DIM.
try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

message = "Enemy defeated!"
if COLOR:
    print(Fore.CYAN + message + Style.RESET_ALL)
else:
    print(message)
