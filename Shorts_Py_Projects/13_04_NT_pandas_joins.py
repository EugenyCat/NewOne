import pandas as pd


"""
The statistics of the company’s clients' transportation services by types are given.
You need to create two tables:

a table with three types of revenue for each client_id without a customer address;
a similar table by type of revenue with the address of the customer.
"""

rzd = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115],
        'rzd_revenue': [1093, 2810, 10283, 5774, 981]
    }
)


auto = pd.DataFrame(
    {
        'client_id': [113, 114, 115, 116, 117],
        'auto_revenue': [57483, 83, 912, 4834, 98]
    }
)


air = pd.DataFrame(
    {
        'client_id': [115, 116, 117, 118],
        'air_revenue': [81, 4, 13, 173]
    }
)


client_base = pd.DataFrame(
    {
        'client_id': [111, 112, 113, 114, 115, 116, 117, 118],
        'address': ['Комсомольская 4', 'Энтузиастов 8а', 'Левобережная 1а', 'Мира 14', 'ЗЖБИиДК 1',
                    'Строителей 18', 'Панфиловская 33', 'Мастеркова 4']
    }
)


client_base_without_adresses = (pd.merge(client_base['client_id'], air, how='left', on='client_id')).merge(auto, how='left', on='client_id').merge(rzd, how='left', on='client_id')
print(client_base_without_adresses)

client_base_with_adresses = pd.merge(client_base, client_base_without_adresses, how='left', on='client_id')
print(client_base_with_adresses)
