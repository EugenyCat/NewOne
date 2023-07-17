import json
import requests
import random
from WordsFromWords import WordsFromWords
from Player import Player
#url:str='https://www.jsonkeeper.com/b/TBIK'


class GameProccess(WordsFromWords, Player):

    def __init__(self, player:str='Player', link:str='https://www.jsonkeeper.com/b/TBIK') -> None:
        self.player = Player(player)
        response = requests.get(link).json()
        response = random.sample(response, k = len(response))[0]
        self.current_word = WordsFromWords(response['word'], set(response['subwords']))


    def to_start_game(self):
        print(f'Complite {self.current_word.count_subwords} words from {self.current_word.main_word}.\nWords have to be from 3 and more letters.')
        user_item = ''

        while  user_item != 'stop' and self.current_word.count_subwords != self.current_word.count_right_answers: 
            print('Input word: ', end='')
            user_item = input()
            self.check_user_input(user_item)


    def to_init_game(self, link:str='https://www.jsonkeeper.com/b/TBIK') -> Player:
        print('Input user name: ')
        user_name = input()
        print(f'Hello, {user_name}')
        return GameProccess(user_name, link)


    def check_user_input(self, user_item:str) -> None:
        if len(user_item) < 3:
            print('Words have to be form 3 and more letters')
        else:
            self.current_word.is_correct(user_item)