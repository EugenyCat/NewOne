"""
easy code with functions
"""

dict_morse = {
    "0": "-----",
    "1": ".----",
    "2": "..---",
    "3": "...--",
    "4": "....-",
    "5": ".....",
    "6": "-....",
    "7": "--...",
    "8": "---..",
    "9": "----.",
    "a": ".-",
    "b": "-...",
    "c": "-.-.",
    "d": "-..",
    "e": ".",
    "f": "..-.",
    "g": "--.",
    "h": "....",
    "i": "..",
    "j": ".---",
    "k": "-.-",
    "l": ".-..",
    "m": "--",
    "n": "-.",
    "o": "---",
    "p": ".--.",
    "q": "--.-",
    "r": ".-.",
    "s": "...",
    "t": "-",
    "u": "..-",
    "v": "...-",
    "w": ".--",
    "x": "-..-",
    "y": "-.--",
    "z": "--..",
    ".": ".-.-.-",
    ",": "--..--",
    "?": "..--..",
    "!": "-.-.--",
    "-": "-....-",
    "/": "-..-.",
    "@": ".--.-.",
    "(": "-.--.",
    ")": "-.--.-"
}


def decode_morse(*word):
    print("Сегодня мы потренируемся расшифровать азбуку Морзе\nнажмите Enter и начнем")
    input()
    answer = {}

    for item in word:
        word_morse = ''
        for i in item:
            word_morse = word_morse + dict_morse[i] + ' '
        print("\nСлово " + str(len(answer)) + ' ' + word_morse)
        user_answer = input("")
        if user_answer == item:
            print("Верно! " + item)
            answer[item] = True
        else:
            print("Неверно! " + item)
            answer[item] = False
    print("\nВсего задачек: " + str(len(answer)))
    print("Отвечено верно: " + str(sum(answer.values())))
    print("Отвечено неверно: " + str(len(answer) - sum(answer.values())))


decode_morse('tree', 'hard', 'porpose', 'python')