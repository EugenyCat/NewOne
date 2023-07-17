"""
The log stream contains number of pages viewed for each user (user, date;views).
You need to write an algorithm that counts average views per user.
It is necessary to calculate the ratio of all views to the number of unique users.

"""

import re


def calculate_average_views(log_list:list) -> int:
    set_user = set()
    score = []
    for record in log_list:
        el = realize_log_file(record)
        set_user.add(el[0])
        score.append(int(el[1]))
    return sum(score)/len(set_user)


def realize_log_file(log_record:str) -> bool:
    user_id = re.search(r'^user\d*', log_record).group()
    #data = re.split(';', re.split(',', log_record)[1])[0]
    count = re.split(';', log_record)[1]
    return [user_id, count]


stream = [
    'user4,2021-01-01;3',
    'user3,2022-01-07;4',
    'user2,2022-03-29;1',
    'user1,2020-04-04;13',
    'user2,2022-01-05;7',
    'user1,2021-06-14;4',
    'user3,2022-07-02;10',
    'user4,2021-03-21;19',
    'user4,2022-03-22;4',
    'user4,2022-04-22;8',
    'user4,2021-05-03;9',
    'user4,2022-05-11;11'
]

print(calculate_average_views(stream))

stream = [
    'user100,2022-01-01;150',
    'user99,2022-01-07;205',
    'user1001,2022-03-29;81'
]

print(calculate_average_views(stream))