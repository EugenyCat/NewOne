"""
Write a function that will return an acronym to the word string.
"""

# https://regex101.com/

import re

some_words = 'Near Field Communication'

def get_acronim(text:str) -> str:
    ret_str = ''
    reg_obj = re.finditer(r'(\s|^)([a-zA-Z])', some_words)
    for item in reg_obj:
        print(item)
        ret_str += item.group(2)
    return ret_str.upper()


print(get_acronim(some_words))