"""
The game with different questions.
"""



import json
import requests
import random

class Question:

    def __init__(self, body:str, level:int, answer:str):
        self.body = body
        self.level = level
        self.answer = answer

        self.status = False
        self.cost = int(level)*10
        self.user_answers = None

        self.commonScore = 0
        self.right_answers = 0
        self.common = 0


    def get_points(self) ->int:
        return self.cost*10

    def is_correct(self, answer) ->bool:
        self.user_answers = answer
        if answer == self.answer:
            self.build_positive_feedback()
            return True
        elif answer != self.answer:
            self.build_negative_feedback()
            return False
        else:
            print('Something is wrong!')
            return False
        
    def build_question(self):
        print(self.body)
        print('Level: {0}/5'.format(self.level))


    def build_positive_feedback(self):
        self.status = True
        self.commonScore += int(self.cost)
        print('Answer is correct. You earn {0}'.format(str(self.cost)))

    def build_negative_feedback(self):
        print('Answer isn\' correct. Right answer is {0}'.format(self.answer))



class Game:
    
    def __init__(self, url='https://www.jsonkeeper.com/b/EHXR'):
        self.url  = url #'https://www.jsonkeeper.com/b/EHXR'
        self.lsonFormLink = requests.get(self.url).json()
        self.list_question = []
        for item in self.lsonFormLink:
            self.list_question.append(Question(item["q"], item["d"], item["a"]))
        
        self.right_answer = 0
        self.score = 0

    def print_statistic(self):
        print("Result:")
        print("Correct answers {0} from {1}".format(self.right_answer, len(self.list_question)))
        print("Your score: {0}".format(self.score))
    
    def start_game(self):

        for item in random.sample(self.list_question, k=len(self.list_question)):
            
            item.build_question()
            answ = input()
            item.user_answers = answ
            
            item.is_correct(answ)
            
            if item.status:
                self.right_answer += 1
                self.score += item.cost

            self.print_statistic()
            

Game('https://www.jsonkeeper.com/b/3H2I').start_game()