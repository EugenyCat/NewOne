#Shift encode
list_alphabet = [
    'a',
    'b',
    'c',
    'd',
    'e',
    'f',
    'g',
    'h',
    'i',
    'j',
    'k',
    'l',
    'm',
    'n',
    'o',
    'p',
    'q',
    'r',
    's',
    't',
    'u',
    'v',
    'w',
    'x',
    'y',
    'z'
]

def shirt_encode(word:str, shift_cnt:int=1) -> str:
    """replacing a letter with the next one by a given shift_cnt"""
    answer = ''
    for i_sym in word:
        if list_alphabet.index(i_sym) + shift_cnt >= len(list_alphabet):
            answer += list_alphabet[abs(len(list_alphabet) - shift_cnt - (list_alphabet.index(i_sym))) ]
        else:
            answer += list_alphabet[list_alphabet.index(i_sym) + shift_cnt]
    #print(answer)
    return answer




def shirt_decode(word, shift_cnt:int=1) -> str:
    """ recieve an original word"""
    answer = ''
    for i_sym in word:
        if list_alphabet.index(i_sym) - shift_cnt < 0:
            answer += list_alphabet[abs(len(list_alphabet) - shift_cnt + (list_alphabet.index(i_sym))) ]
        else:
            answer += list_alphabet[list_alphabet.index(i_sym) - shift_cnt]
    #print(answer)
    return answer


print('Original string: ', 'akcozksywzx')
print('Encode string: ', shirt_encode('akcozksywzx', 2))
print('Decode string: ', shirt_decode(shirt_encode('akcozksywzx', 2), 2))