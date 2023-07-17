"""
Write a function that will remove all consecutive repetitions of words from a given string using regular expressions.
"""

# https://regex101.com/

import re

stg_with_repeats = 'Write a function function, that will remove all all all all consecutive repetitions of words from from from from from ' \
               'of the given string string using regular expressions.'

def delete_repeat(str_with_rep:str) ->str:
    ret_str = str_with_rep
    while re.search(r'([a-zA-Z]{2,})(\s)(\1)', ret_str) is not None:
        #print(re.search(r'([а-яА-Я]+)(\s)(\1)', ret_str))
        ret_str = re.sub(r'([a-zA-Z]{2,})(\s)(\1)', r'\1', ret_str, flags=re.I)
        #print(ret_str)
    return ret_str

print(delete_repeat(stg_with_repeats))