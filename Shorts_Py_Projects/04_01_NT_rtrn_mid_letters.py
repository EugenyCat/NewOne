"""
Given a variable that keeps a word.
Return:
the middle letter if the number of letters in the word is odd;
two middle letters if the number of letters is even.
"""

def to_return_middle_letters(word:str) -> str:
    """define return middle letters form word"""
    if len(word)%2 == 0:
        return word[int(len(word)/2-1)] + word[int(len(word)/2)]
    return word[int(len(word)/2)]

print(to_return_middle_letters('faTHer'))
print(to_return_middle_letters('pycHarm'))
