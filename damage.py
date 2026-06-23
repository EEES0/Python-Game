def get_damage(level) :
    if 0 <= level <= 2:
        return level * 100

    elif 3 <= level <= 5:
        return level * 500

    elif 6 <= level <= 8:
        return level * 1000

    elif 9 <= level <= 11:
        return level * 5000
    elif 12 <= level <= 13:
        return level * 10000
    elif level == 14:
        return 1000000

    return 0