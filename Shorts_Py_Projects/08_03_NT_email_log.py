"""
Write a function that will accept the list of email addresses and display their distribution by domain zones.
"""

# https://regex101.com/

import re

emails = ['test@gmail.com', 'xyz@test.in', 'test@ya.ru', 'xyz@mail.ru', 'xyz@ya.ru', 'xyz@gmail.com']

def email_log(emails:list) -> dict:
    log_email = {}
    for email in emails:
        domain = re.search(r'@([a-zA-Z]*\.[a-z]*)', email).group(1)
        log_email[domain] = 1 if log_email.get(domain) is None else log_email.get(domain) + 1
    return log_email


print(email_log(emails))