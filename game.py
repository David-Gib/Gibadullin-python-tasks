# ================================================
# ИГРА «ОБЛАЧНАЯ БАШНЯ: НЕБЕСНЫЙ ПРИЧАЛ»
# Автор: Давид Гибадуллин
# Дата: Ноябрь 2026
# ================================================

import random
import os
import json

VERSION = "1.0"
MENU_LAST = 12

enemy_stats = {
    "harpy": {"hp": 45, "damage": 6, "loot": 25},
    "gargoyle": {"hp": 30, "damage": 4, "loot": 15},
    "griffin": {"hp": 20, "damage": 3, "loot": 10},
    "cloud_spirit": {"hp": 12, "damage": 2, "loot": 5},
}

prices = {"potion": 10, "torch_oil": 15, "war_elixir": 40}


class Hero:
    def __init__(self, name, health, strength, agility, endurance):
        self.name = name
        self.health = health
        self.strength = strength
        self.agility = agility
        self.endurance = endurance
        self.damage = 10 + strength * 1.5
        self.crit_damage = self.damage * 2
        self.stamina = health // 10 + endurance

    def __str__(self):
        return f"{self.name}: health {self.health}, damage {self.damage:.1f}, stamina {self.stamina}"

    def strike(self, n):
        """Урон героя в удар номер strike_n.
        Возвращает пару (hit, crit): урон и признак критического удара.
        """
        if n % 3 == 0:
            return self.crit_damage, True
        return self.damage, False

    def spend_stamina(self, cost):
        if self.stamina >= cost:
            self.stamina -= cost
            return False
        self.health -= cost - self.stamina
        self.stamina = 0
        return True

    def heal(self, amount, cap):
        self.health = min(self.health + amount, cap)

    def to_dict(self):
        return {
            "name": self.name,
            "health": self.health,
            "stamina": self.stamina,
            "strength": self.strength,
            "agility": self.agility,
            "endurance": self.endurance
        }

    @staticmethod
    def from_dict(data):
        hero = Hero(data["name"], data["health"], data["strength"], data["agility"], data["endurance"])
        hero.stamina = data["stamina"]
        return hero


class Enemy:
    def __init__(self, name, stats):
        self.name = name
        self.hp = stats["hp"]
        self.damage = stats["damage"]
        self.loot = stats["loot"]


def fight(enemy, hero, bonus=0):
    """Бой с enemy до гибели одного из двоих.
    Карточка врага берётся из enemy_stats по имени: нужны ключи
    hp, damage, loot. Печатает строки раундов.
    Возвращает (rounds, won, loot).
    """
    rounds = []
    round_n = 0
    print(f"You descend the stairs. Out of the darkness comes {enemy.name}!")
    while enemy.hp > 0 and hero.health > 0:
        round_n += 1
        hit, crit = hero.strike(round_n)
        hit += bonus
        enemy.hp -= hit
        line = f"Round {round_n}: hero deals {hit:.1f}"
        if crit:
            line += " — critical!"
        if enemy.hp <= 0:
            line += " Enemy falls."
            rounds.append([round_n, hit, 0])
        else:
            blow = enemy.damage
            hero.health -= blow
            line += f" {enemy.name} health: {enemy.hp:.1f}. {enemy.name.capitalize()} hits for {blow}."
            rounds.append([round_n, hit, blow])
        print(line)
    won = enemy.hp <= 0
    loot = enemy.loot if won else 0
    return rounds, won, loot


def buy(price, gold, quantity=1):
    """Покупает quantity штук товара ценой price за золото gold.
    quantity по умолчанию 1. Возвращает (gold_left, ok): остаток
    золота и признак успешной покупки. Ничего не печатает.
    """
    cost = price * quantity
    if gold >= cost:
        return gold - cost, True
    return gold, False


num_to_verb = {
    "1": "look", "2": "go", "3": "rest", "4": "listen",
    "5": "torch", "6": "train", "7": "descend", "8": "leaders",
    "9": "shop", "10": "backpack", "11": "drink", "12": "scout", "0": "exit"
}

commands = [
    "look", "go north", "go south", "go west", "east", "rest", "listen", "torch", "train",
    "descend", "leaders", "shop", "backpack", "drink potion", "scout", "newgame", "exit"
]

MENU = [
    "What do you do? (number or command; help for help)",
    "1 - look around (look)",
    "2 - go forward (go north/south/west/east)",
    "3 - rest (rest)",
    "4 - listen (listen)",
    "5 - light a torch (torch)",
    "6 - train (train)",
    "7 - descend deeper (descend)",
    "8 - leaderboard (leaders)",
    "9 - shop (shop)",
    "10 - backpack (backpack)",
    "11 - drink potion (drink)",
    "12 - scout path (scout)",
    "0 - exit the dungeon (exit)"
]

MAP = [
    ["#", "#", "#", "#", "#"],
    ["#", ".", ".", "#", "#"],
    ["#", ".", "#", ".", "#"],
    ["#", ".", ".", ".", "#"],
    ["#", "#", "S", ".", "#"],
]

DIRECTIONS = {"north": (-1, 0), "south": (1, 0), "west": (0, -1), "east": (0, 1)}
LOOT = {(1, 1): "ancient feather", (2, 3): "sky potion", (3, 3): "griffin's egg"}


def parse_command(line):
    """Возвращает пару (verb, words): глагол и слова команды."""
    cmd = line.strip().lower()
    words = cmd.split()
    if not words:
        return "", []
    verb = words[0]
    if cmd in num_to_verb:
        verb = num_to_verb[cmd]
    return verb, words


def print_leaderboard(log):
    """Печатает топ-3 раундов по урону героя и рекорд врага.
    Возвращает None.
    """
    if not log:
        print("You haven't fought yet.")
        return
    top = sorted(log, key=lambda r: r[1], reverse=True)[:3]
    print("Leaderboard (hero damage):")
    for i in range(len(top)):
        print(f"{i + 1}. Round {top[i][0]}: {top[i][1]:.1f}")
    worst = max(log, key=lambda r: r[2])
    print(f"Strongest enemy hit: {worst[2]} (round {worst[0]}).")


def print_run_summary(log):
    """Печатает итог забега: суммарный и средний урон героя.
    Возвращает None. Безопасна на пустом журнале.
    """
    total = sum(r[1] for r in log)
    rounds = len(log)
    if rounds > 0:
        print(f"Damage: {total:.1f} across {rounds} rounds, average {total / rounds:.1f}.")
    else:
        print("No battles this run.")


def write_save():
    """Собирает состояние забега и пишет его в save.json.
    Кортежи и множества превращает в списки: JSON их не знает.
    Возвращает None.
    """
    save = {
        "hero": hero.to_dict(),
        "gold": gold_total,
        "actions": actions,
        "enemies": enemies,
        "position": [hero_r, hero_c],
        "visited": [list(p) for p in visited],
        "loot": sorted(found_loot),
        "ability_bonus": ability_bonus,
        "max_health": max_health,
        "max_stamina": max_stamina,
        "log": log,
        "inventory": inventory
    }
    with open("save.json", "w", encoding="utf-8") as f:
        json.dump(save, f, ensure_ascii=False, indent=2)


def scout(r, c, seen):
    if (r, c) in seen or MAP[r][c] == "#":
        return 0
    seen.add((r, c))
    total = 1
    for dr, dc in DIRECTIONS.values():
        total += scout(r + dr, c + dc, seen)
    return total


title = "ОБЛАЧНАЯ БАШНЯ: НЕБЕСНЫЙ ПРИЧАЛ"
frame = "=" * 31

print(frame)
print(" " + title + " ")
print(f"  v{VERSION}")
print(frame)
print()

loaded = None
if os.path.exists("save.json"):
    print("A save was found. Continue the run? (yes/no)")
    answer = input().strip().lower()
    if answer == "yes":
        try:
            with open("save.json", encoding="utf-8") as f:
                loaded = json.load(f)
        except json.JSONDecodeError:
            loaded = None

if loaded is None:
    print("Как зовут героя?")
    hero_name = input()
    print(f"Добро пожаловать, {hero_name}!")
    print("Перед тобой парящие в облаках платформы. Гуляет сильный ветер, деревянный настил скрипит.")
    print()

    print("Настройка героя.")
    print("Здоровье, сила, ловкость, выносливость — по одному числу в строке:")

    while True:
        try:
            health = int(input())
            strength = int(input())
            agility = int(input())
            endurance = int(input())
            if health <= 0:
                raise ValueError(f"Здоровье должно быть положительным, а введено {health}")
            if strength < 0 or agility < 0 or endurance < 0:
                raise ValueError("Характеристики не могут быть отрицательными")
            break
        except ValueError as e:
            print(f"{e}. Введите все четыре снова:")

    hero = Hero(hero_name, health, strength, agility, endurance)
    max_health = health
    max_stamina = hero.stamina
    gold_total = 0
    ability_bonus = 0
    enemies = ["harpy", "gargoyle", "griffin", "cloud_spirit"]
    log = []
    inventory = {}
    actions = 0
    hero_r, hero_c = 4, 2
    visited = {(4, 2)}
    found_loot = set()

    print()
    print("Характеристики героя:")
    print(hero)
    print()
else:
    hero = Hero.from_dict(loaded["hero"])
    hero_name = hero.name
    gold_total = loaded["gold"]
    actions = loaded["actions"]
    enemies = loaded["enemies"]
    hero_r, hero_c = loaded["position"]
    visited = {tuple(p) for p in loaded["visited"]}
    found_loot = set(loaded["loot"])
    ability_bonus = loaded["ability_bonus"]
    max_health = loaded["max_health"]
    max_stamina = loaded["max_stamina"]
    log = loaded["log"]
    inventory = loaded["inventory"]
    print(f"Run continued: health {hero.health}, gold {gold_total}, enemies left {len(enemies)}.")

outcome = "прерывание"
running = True

try:
    while running:
        print("\n".join(MENU))
        print()

        while True:
            line = input()
            cmd = line.strip().lower()
            while cmd == "":
                print("Empty command. Type a command or number.")
                line = input()
                cmd = line.strip().lower()
            verb, words = parse_command(line)
            if verb in commands or verb in num_to_verb.values() or verb in DIRECTIONS or verb == "newgame" or verb == "help":
                break
            print(f"Don't understand command: '{line.strip()}'. Type 'help'.")

        match verb:
            case "look":
                print("Вы осмотрелись. Белые облака застилают горизонт, края платформ обрываются в бездну.")

            case "go":
                if len(words) > 1 and words[1] in DIRECTIONS:
                    direction = words[1]
                    dr, dc = DIRECTIONS[direction]
                    nr, nc = hero_r + dr, hero_c + dc
                    if 0 <= nr < len(MAP) and 0 <= nc < len(MAP[nr]) and MAP[nr][nc] != "#":
                        hero_r, hero_c = nr, nc
                        visited.add((hero_r, hero_c))
                        if (hero_r, hero_c) in LOOT:
                            item = LOOT[(hero_r, hero_c)]
                            if item not in found_loot:
                                found_loot.add(item)
                                print(f"You found {item}! Unique loot: {len(found_loot)}.")
                        print(f"You step {direction}. Room ({hero_r}, {hero_c}).")
                    else:
                        print(f"Cannot go {direction}: wall or edge.")
                else:
                    if hero.spend_stamina(2):
                        print("Сил больше нет — вы идёте на одном упорстве.")
                    else:
                        print("Вы осторожно идёте вперёд. Конструкция опасно раскачивается от порывов ветра.")

            case "rest":
                hero.stamina = min(hero.stamina + 5, max_stamina)
                print("Вы садитесь на настил и переводите дух. Силы возвращаются.")

            case "listen":
                print("Вы замираете и слушаете ветер. Сквозь его свист доносится далёкий клёкот крылатых тварей.")

            case "torch":
                if hero.spend_stamina(1):
                    print("Вы слишком устали, чтобы удержать факел против ветра.")
                else:
                    print("Вы зажигаете факел. Ветер яростно раздувает пламя, освещая парящие плиты.")

            case "train":
                strikes = 5
                print("Вы подходите к деревянному столбу перил.")
                print(f"Наносите {strikes} ударов.")
                crit_count = 0
                total_damage = 0
                for i in range(1, strikes + 1):
                    hit_damage, crit = hero.strike(i)
                    if crit:
                        crit_count += 1
                        print(f"Удар {i}: {hit_damage:.1f} — критический!")
                    else:
                        print(f"Удар {i}: {hit_damage:.1f}")
                    total_damage += hit_damage
                hero.stamina = max(0, hero.stamina - 4)
                print(f"Итог: {strikes} ударов, {crit_count} критический.")
                print(f"Общий урон: {total_damage:.1f}")

            case "descend":
                if not enemies:
                    print("You descend the stairs. But the dungeon is empty.")
                else:
                    enemy_name = random.choice(enemies)
                    foe = Enemy(enemy_name, enemy_stats[enemy_name])
                    rounds, won, loot = fight(foe, hero, ability_bonus)
                    for r in rounds:
                        log.append(r)
                    if won:
                        gold_total += loot
                        enemies.remove(enemy_name)
                    print(f"{enemy_name.capitalize()} defeated! {len(enemies)} enemies left in the dungeon. Loot: {loot} gold.")
                    print(f"Battle: {len(rounds)} rounds.")

            case "leaders":
                print_leaderboard(log)

            case "shop":
                print("Shop:")
                for name, price in prices.items():
                    print(f"{name}: {price} gold")
                print("Item name (empty line — not buying):")
                name = input().strip().lower()
                if name != "":
                    if name in prices:
                        price = prices[name]
                        print("Quantity (Enter for one):")
                        qty_line = input()
                        if qty_line == "":
                            qty = 1
                            gold_total, ok = buy(price, gold_total)
                        else:
                            qty = int(qty_line)
                            gold_total, ok = buy(price, gold_total, quantity=qty)
                        if ok:
                            inventory[name] = inventory.get(name, 0) + qty
                            if name == "potion":
                                hero.heal(10 * qty, max_health)
                            elif name == "torch_oil":
                                hero.stamina = min(hero.stamina + 5 * qty, max_stamina)
                            else:
                                ability_bonus += 2 * qty
                            print(f"Bought {qty} {name} for {price * qty} gold. Gold left: {gold_total}.")
                        else:
                            print(f"Not enough gold: need {price * qty}, have {gold_total}.")
                    else:
                        print("No such item in the shop.")

            case "backpack":
                if not inventory:
                    print("Backpack is empty.")
                else:
                    print("Backpack:")
                    for name, qty in inventory.items():
                        print(f"{name}: {qty} pcs")

            case "drink":
                if inventory.get("potion", 0) == 0:
                    print("No potions in the backpack.")
                else:
                    hero.heal(10, max_health)
                    inventory["potion"] -= 1
                    if inventory["potion"] == 0:
                        del inventory["potion"]
                    print(f"You drink a potion. Health: {hero.health}. Potions left: {inventory.get('potion', 0)}.")

            case "scout":
                seen = set()
                print(f"Scout: {scout(hero_r, hero_c, seen)} rooms reachable.")

            case "newgame":
                if os.path.exists("save.json"):
                    os.remove("save.json")
                print("Save destroyed. The next run starts fresh.")
                continue

            case "help":
                print("Commands: " + ", ".join(commands) + ".")
                print("Numbers 0-12 work as before.")

            case "exit":
                print("Вы спускаетесь по веревочной лестнице к подножию. Облачная башня остаётся позади.")
                write_save()
                print("Progress saved.")
                outcome = "выход"
                running = False

        if hero.health <= 0:
            print(f"{hero_name} падает без сил. Облачная башня забирает ещё одного искателя.")
            if os.path.exists("save.json"):
                os.remove("save.json")
            outcome = "гибель"
            running = False

        if running:
            actions += 1
            print()
            print(f"Health: {hero.health} Stamina: {hero.stamina} Enemies left: {len(enemies)} Gold: {gold_total}")

except KeyboardInterrupt:
    print()
    print("The player ended the session.")
    write_save()

finally:
    print(frame)
    if outcome == "гибель":
        print(f"Ты не дошёл, {hero_name}. Действий совершено: {actions}.")
    elif outcome == "выход":
        print(f"Забег окончен, {hero_name}. Действий совершено: {actions}.")
    else:
        print(f"Сеанс прерван, {hero_name}. Действий совершено: {actions}.")
    if inventory:
        print("Left behind in the backpack:")
        for name, qty in inventory.items():
            print(f"{name}: {qty} pcs")
    else:
        print("Left behind in the backpack: nothing.")
    print_run_summary(log)
    print(frame)


if __name__ == "__main__":
    test_hero = Hero("Тест", 100, 7, 5, 4)
    test_foe = Enemy("harpy", enemy_stats["harpy"])
    r_data, is_won, drop = fight(test_foe, test_hero)
    print(f"self-test: {len(r_data)} rounds, won={is_won}, loot={drop}")
