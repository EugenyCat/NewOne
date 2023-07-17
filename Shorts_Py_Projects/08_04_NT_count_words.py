"""
Write a function that will count how many words start with vowels and how many with consonants in the text. Text can be written using both Cyrillic and Latin letters.
"""

# https://regex101.com/

import re

some_text = 'The benchmark implementation of Python is the CPython interpreter, which supports most of the platforms in active use. ' \
            'It is distributed under the free Python Software Foundation License, allowing it to be used without restriction in any applications, including proprietary applications.'

def count_words(text:list) -> list:
    vowel = 'aeiouyAEIOUY'
    return [len(re.findall(rf'(^|\s)([{vowel}]\w*)', text)), len(re.findall(rf'(^|\s)([^{vowel}]\w*)', text))]


print(f'Words on vowel letters: {count_words(some_text)[0]}\nWords on consonant letters: {count_words(some_text)[1]}')