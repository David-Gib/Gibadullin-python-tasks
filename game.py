# ================================================
# ИГРА «ПОДЗЕМЕЛЬЕ: ТИХИЙ КОЛОДЕЦ»
# Автор: Гибадуллин Давид
# Дата: октябрь 2026
#
# Меню: 1-5 — обычные действия, 6 — тренировка, 0 — выход.
# Пункт 4 — «прислушаться»: герой замирает и слушает темноту, это бесплатно.
# Пункт 5 — «зажечь факел»: тратит 1 запас сил.
#
# Мои решения:
# - четыре характеристики читаются одним циклом: набор либо принят целиком,
#   либо перечитывается весь заново;
# - дорога тратит 2 силы, тренировка 3, отдых даёт 3;
# - отдых не поднимает запас сил выше стартового значения (max_stamina).
# ================================================

# --- Заголовок ------------------------------------
title = "ПОДЗЕМЕЛЬЕ: ТИХИЙ КОЛОДЕЦ"
frame = "=" * 31

print(frame)
print("   " + title + "   ")
print(frame)
print()

# --- Знакомство с героем --------------------------
print("Как зовут героя?")
hero_name = input()
print(f"Добро пожаловать, {hero_name}!")
print("Ты входишь в подземелье. Здесь темно и пахнет сыростью.")
print()

# --- Настройка героя -------------------------------
print("Настройка героя.")
print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")

while True:
    # формат: сами числа читаются в узком try
    try:
        health = int(input())
        strength = int(input())
        agility = int(input())
        endurance = int(input())
    except ValueError:
        print("Ой: одна из строк не число. Введите все четыре снова:")
        continue
    # смысл: свои правила через raise
    try:
        if health <= 0:
            raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
        if strength < 0 or agility < 0 or endurance < 0:
            raise ValueError("Характеристики не могут быть отрицательными")
        if strength > 30:
            raise ValueError(f"Сила не может быть больше 30, а введено {strength}")
        break
    except ValueError as e:
        print(f"{e}. Введите все четыре снова:")

# --- Расчёт урона ----------------------------------
base_attack = 10
damage = base_attack + strength * 1.5
crit_damage = damage * 2
stamina = health // 10 + endurance
max_stamina = stamina

# --- Формуляр героя --------------------------------
print("Характеристики героя:")
print(f"Здоровье:     {health}")
print(f"Сила:         {strength}")
print(f"Ловкость:     {agility}")
print(f"Выносливость: {endurance}")
print()
print(f"Урон героя:       {damage:.1f}")
print(f"Критический урон: {crit_damage:.1f}")
print(f"Запас сил:        {stamina}")
print()

# --- Главный цикл игры -----------------------------
running = True
actions = 0
menu_last = 6
outcome = "прерывание"

try:
    while running:
        print("Что делаешь?")
        print("1 - осмотреться")
        print("2 - идти вперёд")
        print("3 - отдохнуть")
        print("4 - прислушаться")
        print("5 - зажечь факел")
        print("6 - тренировка")
        print("0 - выйти из подземелья")

        # --- Защита выбора: перечитываем, пока не придёт номер из меню
        while True:
            choice = input()
            try:
                menu_number = int(choice)
            except ValueError:
                print("Такого пункта нет. Введи номер пункта из меню.")
                continue
            if 0 <= menu_number <= menu_last:
                break
            print("Такого пункта нет. Введи номер пункта из меню.")
            
        choice = str(menu_number)

        # --- Выбор действия ----------------------------
        match choice:
            case "1":
                print("Вы осмотрелись. Стены в сырых разводах, на полу темнеет вода.")

            case "2":
                cost = 2
                if stamina >= cost:
                    stamina -= cost
                    print("Вы осторожно идёте вперёд. Пол скрипит под ногами.")
                else:
                    health -= cost - stamina
                    stamina = 0
                    if health < 0:
                        health = 0
                    print("Сил больше нет — вы идёте на одном упорстве.")

            case "3":
                stamina += 3
                if stamina > max_stamina:
                    stamina = max_stamina
                print("Вы садитесь на пол и переводите дух. Силы возвращаются.")

            case "4":
                print("Вы замираете и слушаете. Где-то капает вода, а дальше — тишина.")

            case "5":
                if stamina >= 1:
                    stamina -= 1
                    print("Вы зажигаете факел. Тени разбегаются по стенам.")
                else:
                    print("Сил не хватает даже на то, чтобы высечь искру.")

            case "6":
                strikes = 6
                train_cost = 3
                if stamina < train_cost:
                    print("Вы слишком устали для тренировки. Нужно отдохнуть.")
                else:
                    stamina -= train_cost
                    print("Вы подходите к тренировочному чучелу.")
                    print("Оно стоит здесь с тех пор, как сюда приходил последний искатель.")
                    print()
                    print(f"Наносите {strikes} ударов.")
                    total_damage = 0
                    crit_count = 0
                    for i in range(1, strikes + 1):
                        if i % 3 == 0:
                            hit_damage = crit_damage
                            crit_count += 1
                            print(f"Удар {i}: {hit_damage:.1f} — критический!")
                        else:
                            hit_damage = damage
                            print(f"Удар {i}: {hit_damage:.1f}")
                        total_damage += hit_damage
                    print()
                    print(f"Итог: ударов — {strikes}, критических ударов: {crit_count}")
                    print(f"Общий урон: {total_damage:.1f}")
                    print(f"Средний урон: {total_damage / strikes:.1f}")

            case "0":
                print("Вы поднимаетесь обратно к свету. Подземелье остаётся позади.")
                outcome = "выход"
                running = False

            case _:
                print("Такого действия нет.")

        # --- Счётчик действий и строка состояния -------
        if running:
            actions += 1
            print()
            print(f"Здоровье: {health} Запас сил: {stamina}")

        # --- Проверка гибели ---------------------------
        if health <= 0:
            print(f"{hero_name} падает без сил. Подземелье забирает ещё одного искателя.")
            outcome = "гибель"
            running = False

except KeyboardInterrupt:
    print()
    print("Игрок прервал сеанс.")

finally:
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    print(frame)
