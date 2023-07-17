"""
Given the variable, which stores statistics of advertising channels by sales volume.
Write a program that returns the channel name with maximum sales.
"""

def get_max_value(sales:dict) -> str:
    """Return max value from dictionary"""
    return search_in_dict(sales, max(sales.values()))

def search_in_dict(sales:dict, val:int) -> str:
    """Loop for elements of dictionary. Return Key if value == val"""
    for el in sales:
        if val == sales.get(el):
            return el
    return None

stats = {'facebook': 55, 'yandex': 115, 'vk': 120, 'google': 99, 'email': 42, 'ok': 98}

print(get_max_value(stats))