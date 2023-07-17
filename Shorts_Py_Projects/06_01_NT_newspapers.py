"""
For each newspaper from the list write the format of the specified date to be transferred to the datetime object
"""

"""https://www.w3schools.com/python/python_datetime.asp"""


from datetime import datetime


def read_date(magazine_date:str, magazine:str) -> datetime:
    """
    Return datetime object for each newspaper's format.
    """
    if magazine == 'The Moscow Times':
        return datetime.strptime(str(magazine_date), '%A, %B %d, %Y')
    elif magazine == 'The Guardian':
        return datetime.strptime(str(magazine_date), '%A, %d.%m.%y')
    elif magazine == 'Daily News':
        return datetime.strptime(str(magazine_date), '%A, %d %B %Y')
    return 'Unknown magazine name'


print(read_date('Wednesday, October 2, 2002', 'The Moscow Times'))
print(read_date('Friday, 11.10.13', 'The Guardian'))
print(read_date('Thursday, 18 August 1977', 'Daily News'))
print(read_date('Thursday, 18 August 1977', 'Magazine'))








