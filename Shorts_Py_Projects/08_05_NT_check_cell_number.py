"""
Write a function that will check cell phone number for validity, only for Russian format. If it is valid, then convert it to the format:
+7-xxx-xxx-xx-xx
"""

# https://regex101.com/

import re
from typing import Tuple

phone = ['+7 955 555-55-55', '8(955)555-55-55', '+7 955 555 55 55', '7(955) 555-55-55', '423-555-55-5555', '123-456-789']


def count_words(phones:list) -> tuple[int, int]:
    correct_phones = {}
    for phone in phones:
        check_phone = re.search(r'^(\+7|8|7)(\s|\()([\d]{3})(\s|\-|\)\s|\))([\d]{3})(\-|\s)([\d]{2})(\-|\s)([\d]{2})', phone)
        if check_phone is not None:
            correct_phones[phone] = f'+7-{check_phone.group(3)}-{check_phone.group(5)}-{check_phone.group(7)}-{check_phone.group(9)}'
        else:
            correct_phones[phone] = 'Number is not validated'
    return correct_phones

print(count_words(phone))
