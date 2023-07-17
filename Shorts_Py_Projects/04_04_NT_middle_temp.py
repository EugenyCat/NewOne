"""
We have a list containing information on the average day temperature in the Fahrenheit for any given period by country.
It is necessary to write a code that calculates the average temperature for the period in Celsius(!) for each country.
"""

def calculate_middle_temp(list_temperatures:list) -> list:
    list_middle_temperat = {}
    for item in list_temperatures:
        list_middle_temperat[item[0]] = (sum(item[1]) / len(item[1]) - 32) * 5 / 9
    return list_middle_temperat


countries_temperature = [
    ['Таиланд', [75.2, 77, 78.8, 73.4, 68, 75.2, 77]],
    ['Германия', [57.2, 55.4, 59, 59, 53.6]],
    ['Россия', [35.6, 37.4, 39.2, 41, 42.8, 39.2, 35.6]],
    ['Польша', [50, 50, 53.6, 57.2, 55.4, 55.4]]
]


print(calculate_middle_temp(countries_temperature))