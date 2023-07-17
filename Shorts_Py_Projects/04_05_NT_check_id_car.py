"""
There is a list with transport numbers.
It is necessary to write a code that will check each number for validity
(1 letter, 3 digits, 2 letters, 2-3 digits). 2
Note that not all letters of the Cyrillic alphabet are used in transport numbers.
"""

import re

car_ids = ['А222ВС96', 'АБ22ВВ193', 'А122ВВ193', 'А122ВВ3', 'Б122ВВ193']


def prepare_checked_list(car_id:list) -> list:
    list_checked_id = {}
    for _id in car_id:
        list_checked_id[_id] = check_id_car(_id)
    return list_checked_id

def check_id_car(car_id:str) -> bool:
    """Check car id. Return True or False. There are Russian alfabet"""
    permitted_symbols = 'А, В, Е, К, М, Н, О, Р, С, Т, X, У'
    return re.search(rf'^[{permitted_symbols}]\d{{3}}[{permitted_symbols}]{{2}}\d{{2,3}}$', car_id) is not None


print(prepare_checked_list(car_ids))