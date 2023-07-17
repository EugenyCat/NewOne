"""
Given a variable that stores a dictionary containing geo-labels for each user.
You need to write a program that will display many unique geo-labels of all users.
"""

def return_uniq_geo(dict_geo:dict) -> set:
    set_geo = set()
    for geo in dict_geo.values():
        set_geo = set_geo.union(set(geo))
    return set_geo

ids = {'user1': [213, 213, 213, 15, 213],
       'user2': [54, 54, 119, 119, 119],
       'user3': [213, 98, 98, 35]}

print(return_uniq_geo(ids))



















