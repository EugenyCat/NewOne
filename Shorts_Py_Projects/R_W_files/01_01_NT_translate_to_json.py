"""
Translate the contents of the purchase_log.txt into a  dictionary of the form:
{'1840e0b9d4': 'Products', ...}
"""


import json

#Realization 1
with open('files/purchase_log.txt', 'r', encoding='utf-8') as f:
    f.readline()
    purchase_dict = {}
    for line in range(f.__sizeof__()):
        dect_el = f.readline().strip('{').rstrip('}\n')
        user_id = dect_el.split(',')[0].split(':')[1].strip(' \"')
        category = dect_el.split(',')[1].split(':')[1].strip(' \"')
        purchase_dict[user_id] = category
    print(purchase_dict)


#Realization 2
with open('files/purchase_log.txt', 'r', encoding='utf-8') as f:
    f.readline()
    purchase_dict = {}
    for line in range(f.__sizeof__()):
        json_el = json.loads(f.readline())
        purchase_dict[json_el.get('user_id')] = json_el.get('category')
    print(purchase_dict)


