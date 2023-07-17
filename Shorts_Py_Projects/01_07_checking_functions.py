# Checking functions
import re


def check_pin(pin: int) -> bool:
    """ """
    if len(str(pin)) != 4 or pin == 1234 or str(pin).count(str(pin)[0]) == 4:
        return False
    else:
        return True


check_pin(1235)


def check_pass(pswrd: str) -> bool:
    """ """

    if len(pswrd) < 8 or re.search(r'\d', pswrd) == None or re.search(r'[a-zA-Z]', pswrd) == None:
        return False
    else:
        return True


check_pass('asdasdasd121das')


def check_mail(mail: str) -> bool:
    """ """
    if re.search(r'..@..', mail) == None or re.search(r'..\...', mail) == None or re.search(r'@\.', mail) != None:
        return False
    else:
        return True


check_mail('as@.ru')


def check_name(name: str) -> bool:
    """Check containing only Russian symbols """
    if re.search(r'[а-я А-Я]', name) == None or re.search(r'[^а-я А-Я]', name) != None:
        return False
    else:
        return True


print(check_name('Маша Вася'))