
"""
For each user_id in the visit_log.csv file, define the third column with the purchase category,
if there was a purchase, the visit_log.csv file itself does not need to be changed.
Record the visits from the visit_log.csv file into the funnel.csv file, which included purchases with a category.
Consider data conditions:
the content of purchase_log.txt is placed in the computer's RAM;
contents of visit_log.csv - no; use only line-by-line processing of this file.
"""

import json


with open('files/purchase_log.txt', 'r', encoding='utf-8') as f:
    f.readline()
    purchase_dict = {}
    for line in range(f.__sizeof__()):
        json_el = json.loads(f.readline())
        purchase_dict[json_el.get('user_id')] = json_el.get('category')
    f.close()


with open('files/visit_log.csv', 'r', encoding='utf-8') as fr:
    fr.readline()
    with open('files/funnel.csv', 'w', encoding='utf-8') as fw:
        fw.write('user_id,source,category\n')
        for line in range(fr.__sizeof__()):
            read_line = fr.readline().strip('\n')
            purchase_category = purchase_dict.get(read_line.split(',')[0]) if purchase_dict.get(read_line.split(',')[0]) is not None else ''
            fw.write(f'{read_line},{purchase_category}\n')
        fr.close()
        fw.close()
purchase_dict = {}



