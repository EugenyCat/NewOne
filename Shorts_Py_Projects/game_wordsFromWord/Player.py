class Player():

    def __init__(self, username:str) -> None:
        self.user_name = username
        self.list_guess_words = []

    def to_add_word(self, word:str) -> None:
        self.list_guess_words.append(word)