"""
YYYY-MM-DD date stream with incorrect values is given.
Write a function that checks these dates for correctness.
That is, for each date returns True - the date is correct or False - incorrect.
"""

"""https://www.w3schools.com/python/python_datetime.asp"""



from datetime import datetime


def determine_status_date(stream_date:list) -> dict:
    """
    Calculate: True or False Date
    """
    stream_checked = {}
    for str_date in stream_date:
        try:
            datetime.strptime(str_date, '%Y-%m-%d')
            stream_checked[str_date] = True
        except ValueError:
            stream_checked[str_date] = False
    return stream_checked


stream = ['2018-04-02', '2018-02-29', '2018-19-02']
print(determine_status_date(stream))