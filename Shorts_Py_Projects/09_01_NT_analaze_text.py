"""
1. Count the number of characters in a string, excluding spaces.
2. Count the number of words in the line.
3. Write a function that will accept a letter as an argument and infer all words from the string beginning with that letter (for example, "w").
"""

import re


string_01 = "History is always written by the winners. When two cultures clash, the loser is obliterated, and the " \
            "winner writes the history books - books which glorify their own cause and disparage the conquered foe. " \
            "As Napoleon once said, 'What is history, but a fable agreed upon?'"


# 1. Count the number of characters in a string, excluding spaces.
count = 0
for item in string_01:
    if item != ' ':
        count += 1
print(count)

print(len(re.findall(r'[\S]', string_01)))


#2. Count the number of words in the line.
count = 0
for item in string_01:
    if item == ' ':
        count += 1
print(count)

print(len(re.findall(r'[a-zA-Z]+', string_01)))


#3. Write a function that will accept a letter as an argument and infer all words from the string
#   beginning with that letter (for example, "w").

def search_words_become_with_letter(text:str, letter:str) -> list:
    return set(re.findall(rf'^|\s({letter}[a-zA-Z]*)', text)[1:])

print(search_words_become_with_letter(string_01, 'w'))


def search_words_become_with_letter(text:str, letter:str) -> list:
    res_list = set()
    for word in text.split(' '):
        if word[0] == letter:
            res_list.add(word.strip('.'))
    return res_list

print(search_words_become_with_letter(string_01, 'w'))




