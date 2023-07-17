"""
The game jeopardy.
"""


import json


""" self_game = {
    "transport": {
        "100": {"question": "самолет"   , "answer": "plane"     , "asked": False},
        "200": {"question": "поезд"     , "answer": "train"     , "asked": False},
        "300": {"question": "посадка"   , "answer": "boarding"  , "asked": False}
    },
    "animals": {
        "100": {"question": "собака", "answer": "dog", "asked": False},
        "200": {"question": "акула", "answer": "shark", "asked": False},
        "300": {"question": "воробей", "answer": "sparrow", "asked": False}
    },
    "food": {
        "100": {"question": "яблоко", "answer": "apple", "asked": False},
        "200": {"question": "ягода", "answer": "berry", "asked": False},
        "300": {"question": "олениа", "answer": "venision", "asked": False}
    }
}

json.dump(self_game, open('..//txts drafts//selfgame.json', 'w', encoding='utf-8'), ensure_ascii=False) """


def read_qustions() -> dict:
    data = json.load(open('txts drafts//selfgame.json', 'r', encoding='utf-8'))
    return(data)


def output_questions(qstns:dict):
    for item in qstns:
        print(item, end='    \t')
        for cont in qstns[item]:
            #print(qstns[item].get(cont)['asked'], end=' ')
            if qstns[item].get(cont)['asked'] == False:
                print(cont, end='\t')
            else:
                print('   ', end='\t')
        print()

def check_input(topic, qstns:dict) ->bool:
    row = qstns.get(topic.split(' ')[0])
    if row == None:
        column = None
    else:
        column = row.get(topic.split(' ')[1])
    if row == None or column == None:
        return False
    else:
        return True


def print_user_statistic(res:dict) -> bool:
    print('\nQuestions are over.')
    print('Your score: ' + str(res['user_score']))
    print('Count of correct answers: ' + str(res['correct_count']))
    print('Count of incorrect answers: ' + str(res['incorrect_count']))
    return True

def save_res_to_file(res:dict, user:str) ->bool:
    resJSON = {
        "user": user,
        "result": res
    }
    with open('txts drafts//selfgame_results.json', 'a', encoding='utf-8') as rf:
        json.dump(resJSON, rf, ensure_ascii=False)
        rf.write('\n')
        


def game_proccess() ->bool:
    user_name = ''
    while len(user_name) == 0:
        print('Please, input your name!')
        user_name = input()

    print('Hello, ', user_name, '\nLet start!\n')
    
    qustions_dict = read_qustions()
    countIter = len(qustions_dict) * len(qustions_dict[list(qustions_dict.keys())[0]])

    user_statistic = {
        "user_score": 0,
        "correct_count": 0,
        "incorrect_count": 0
    }
    for iter in range(countIter):
        print('Select the one of that items')
        
        output_questions(qustions_dict)

        cur_question = ''
        while len(cur_question)==0 and not check_input(cur_question, qustions_dict):
            cur_question = input()
            if not(check_input(cur_question+' er', qustions_dict)):
                cur_question = ''
                print('Ups! Something is wrong. Repeat please!')
            else:
                question_word = qustions_dict.get(cur_question.split(' ')[0]).get(cur_question.split(' ')[1]).get('question')
                right_answer = qustions_dict.get(cur_question.split(' ')[0]).get(cur_question.split(' ')[1]).get('answer')
                print('Word ' + question_word + ' is meaning: ')
                user_answ = input()
                if right_answer == user_answ:
                    user_statistic["user_score"] += int(cur_question.split(' ')[1])
                    user_statistic["correct_count"] += 1
                    print('Right! +' +cur_question.split(' ')[1] + '. Your score ' + str(user_statistic["user_score"]))
                else:
                    user_statistic["user_score"] -= int(cur_question.split(' ')[1])
                    user_statistic["incorrect_count"] += 1
                    print('Incorrect! -' +cur_question.split(' ')[1] + '. Your score ' + str(user_statistic["user_score"]))

                qustions_dict.get(cur_question.split(' ')[0]).get(cur_question.split(' ')[1])['asked'] = True
    
    print_user_statistic(user_statistic)
    save_res_to_file(user_statistic, user_name)



    

game_proccess()