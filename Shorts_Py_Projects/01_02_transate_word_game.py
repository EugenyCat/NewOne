"""
easy code with dictionary
"""

dict_levels = {"easy": "easy", "medium": "medium", "hard": "hard"}
dict_easy = {"уровень": "level", "предложение": "proposal", "цель": "aim"}
dict_medium = {"средний": "medium", "земля": "earth", "пропустить": "pass"}
dict_hard = {"сложный": "hard", "убить": "kill", "занимать": "borrow"}
answers = {}

# Choose level
print('Select level')
vSelect = True;
while vSelect:
    level = input("")
    for keys in dict_levels:
        if level == dict_levels[keys]:
            print("You choose " + level + ", we prefer 3 words, input translate")
            if level == 'easy':
                dict_words = dict_easy
            elif level == 'medium':
                dict_words = dict_medium
            else:
                dict_words = dict_hard
            vSelect = False

    if vSelect:
        print("Uncorrect! Choose from this: easy, medium, hard")

# Введите Enter
vSelect = True;
countBalls = 0
while vSelect:
    print('Click Enter')
    emptyString = input()
    if len(emptyString) == 0:
        for keys in dict_words:
            print(keys + ", " + str(len(dict_words[keys])) + " letters, begin on " + dict_words[keys][0])
            userAnswer = input("")
            if (userAnswer == dict_words[keys]):
                print("Good, " + keys + " is " + dict_words[keys])
                answers[keys] = True
                countBalls += 1
            else:
                answers[keys] = False
                print("Bad. " + keys + " is " + dict_words[keys])

        print("\nCorrects answers:")
        for i in answers:
            if answers[i] == True:
                print(i)
        print("\nUncorrect answers:")
        for i in answers:
            if answers[i] == False:
                print(i + '\n')
        print("\nYour score: " + str(countBalls))
        vSelect = False