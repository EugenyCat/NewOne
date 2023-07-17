class WordsFromWords():

    def __init__(self, main_word:str, set_subwords:set) -> None:
        self.count_right_answers = 0
        self.main_word = str.upper(main_word)
        self.subwords = {}
        for item in set_subwords:
            self.subwords[item] = False
        self.count_subwords = len(set_subwords)

    
    def is_correct(self, user_word:str) -> None:
        if user_word == 'stop':
            self.game_over()
        elif self.subwords.get(user_word) == False:
            self.subwords[user_word] = True
            self.to_count_result()
        elif self.subwords.get(user_word) == True:
            print('That word already was guessed.')
        elif self.subwords.get(user_word) == None:
            print('Please, try another word.')


    def to_count_result(self) -> None:
        self.count_right_answers += 1
        print('Right')
        if self.count_right_answers == self.count_subwords:
            self.game_over()


    def game_over(self) -> None:
        print(f'\nGame over. You guess {self.count_right_answers} word(s)')


    def __repr__(self) -> str:
        return f"WordsFromWords('{self.main_word, self.subwords}')"