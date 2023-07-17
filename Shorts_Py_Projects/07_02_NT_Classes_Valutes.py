"""
Task 1
Write a function that returns the currency name with the maximum value.

Task 2
Create class Rate with methods that return 1) value of currency 2) whole information about currency.
Add the diff parameter (with True or False values) to the Rate class, which in the case of True
will not return the exchange rate, but a change from the previous value.
Consider that self_diff will only take True when the exchange rate is returned.
"""


import requests


class Rate:

    def __init__(self, format:str='value', diff:bool=False):
        self.format = format
        self.diff = diff
        self.currencies = requests.get('https://www.cbr-xml-daily.ru/daily_json.js').json()["Valute"]

    #Task 1
    def get_max_currency(self) -> str:
        """
        Return currency name with max value.
        """
        return max([item["Value"] for item in list(self.currencies.values())])


    def get_currency(self, valute_name:str='USD'):
        """
        Return information about currency.
        """
        if self.format == 'full':
            return self.get_full_currency(valute_name)
        else:
            return self.get_value_currency(valute_name)


    def get_full_currency(self, valute_name:str='USD'):
        """
        Return whole information about currency.
        """
        if self.diff:
            currencies = self.currencies.get(valute_name)
            currencies['diff'] = round(currencies.get('Value') - currencies.get('Previous'), 4)
            return currencies
        else:
            return self.currencies.get(valute_name)


    def get_value_currency(self, valute_name:str='USD'):
        """
        Return value currency.
        """
        if self.diff:
            return round(self.currencies.get(valute_name).get('Value') - self.currencies.get(valute_name).get('Previous'), 4)
        else:
            return self.currencies.get(valute_name)['Value']


r = Rate()
print(r.get_max_currency())
print(r.get_currency())

r = Rate(diff=True)
print(Rate(diff=True).get_currency())

r = Rate(format='full')
print(r.get_currency(valute_name='EUR'))

r = Rate(format='full', diff=True)
print(r.get_currency(valute_name='EUR'))