import random


def get_upgrade_cost(level):

    if 0 <= level <= 2:
        return level * 100

    elif 3 <= level <= 5:
        return level * 300

    elif 6 <= level <= 8:
        return level * 500

    elif 9 <= level <= 11:
        return level * 1000

    elif 12 <= level <= 13:
        return level * 3000

    return 0


def get_sell_price(level):

    if 0 <= level <= 2:
        return level * 200

    elif 3 <= level <= 5:
        return level * 1000

    elif 6 <= level <= 8:
        return level * 3000

    elif 9 <= level <= 11:
        return level * 5000

    elif 12 <= level <= 13:
        return level * 10000

    elif level == 14:
        return 500000

    return 0


def get_upgrade_percent(level):

    return max(100 - level * 5, 20)


def try_upgrade(level, gold, bonus_percent = 0):

    if level >= 14:
        return level, gold

    cost = get_upgrade_cost(level)
    percent = bonus_percent or get_upgrade_percent(level)
    if gold < cost:
        return level, gold
    rand = random.randint(1, 100)
    if rand <= percent:

        level += 1
        gold -= cost

    else:

        level = 0
        gold -= cost

    return level, gold


def sell_item(level, gold):

    gold += get_sell_price(level)

    level = 0

    return level, gold