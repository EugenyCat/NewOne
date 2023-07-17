"""
Write the date_range function, which returns a list of dates from start_date to end_date.
Dates must be entered in YYYY-MM-DD format.
In case of incorrect format or if start_date > end_date should return an empty list.
"""

"""https://www.w3schools.com/python/python_datetime.asp"""



from datetime import datetime, timedelta


def date_range(start_date:str, end_date:str) -> list:
    """
    Return list of dates from start_date to end_date
    Format date: YYYY-MM-DD
    Conditional: if format incorrect or start_date > end_date-> return []
    """
    list_range = []
    try:
        start_datetime_obj = datetime.strptime(start_date, '%Y-%m-%d')
        end_datetime_obj = datetime.strptime(end_date, '%Y-%m-%d')
        if start_date > end_date:
            raise  ValueError
    except ValueError:
        return list_range

    list_range.append(datetime.strftime(start_datetime_obj, '%Y-%m-%d'))
    while start_datetime_obj < end_datetime_obj:
        start_datetime_obj += timedelta(days=1)
        list_range.append(datetime.strftime(start_datetime_obj, '%Y-%m-%d'))
    return list_range


print(date_range('2023-03-01', '2023-03-05'))
