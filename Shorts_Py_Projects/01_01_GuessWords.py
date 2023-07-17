"""
The Game where user input self name, and after that he has to guess word.
Program print words with mixed up letters.
In the end program has to print common result of game.
"""


import random



def open_file() -> list:
    """Open file and create list"""
    f = open('txts drafts\\words.txt', 'r')
    list_words = []
    for line in f:
        list_words.append(line.replace('\n', ''))
    f.close()
    return list_words


def write_file(user:str, score:int) -> bool:
    """Write result in histore.txt"""
    with open('txts drafts\\history.txt', 'a') as f:
        f.write(user + ' ' + str(score) + '\n')

    f = open('txts drafts\\history.txt', 'r')
    list_words = []
    for line in f:
        list_words.append(line.replace('\n', '').split(' ', 1)[1])
    f.close()
    print('The best result: ', max(list_words))
    return True


def guess_words() -> bool:
    """Game - Guess words"""
    list_words = open_file()

    print(list_words[0])
    user_name = ''
    if len(user_name) == 0:
        print('Imput your name: ')
        user_name = input()

    count = 0
    for item in range(len(list_words)):
        answer_word = ''
        #.sample(x, len(x)) - replace elements with each other
        print('\nGuess word: ', *random.sample(list_words[item], k=len(list_words[item])))
        answer_word = input()
        if  answer_word == list_words[item]:
            print("Right! You get a 10 balls!")
            count += 10
        else:
            print('Sorry! You lose:(')

    print('Your score: ', str(count)) 
    write_file(user_name, count)
    
    return True



guess_words()