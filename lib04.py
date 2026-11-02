# Задание: Lib4. Подключить colorama с откатом: try-import и флаг COLOR; строка состояния зелёная при COLOR и обычная без библиотеки. Проверка: запуск без активации venv не падает.

try:
    from colorama import Fore, Style, init
    init()
    COLOR = True
except ImportError:
    COLOR = False

state = "Health: 100 Stamina: 10 Gold: 0"
if COLOR:
    print(Fore.GREEN + state + Style.RESET_ALL)
else:
    print(state)
