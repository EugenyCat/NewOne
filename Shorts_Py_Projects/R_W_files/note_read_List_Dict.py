import json
import note_pickle_and_OS

with open('files/purchase_log.txt', encoding='utf-8') as f:
    print([next(f) for x in range(5)])


"""Translate line in dictionary"""
dict_in_string = '{"a": 1, "b": 2}'

type(json.loads(dict_in_string))
json.loads(dict_in_string)

i = 0
with open('files/purchase_log.txt', encoding='utf-8') as f:
    for line in f:
        line = line.strip()

        dict_ = json.loads(line)
        print(dict_, type(dict_))

        i += 1
        if i > 5:
            break

"""Dict to str"""
data = {'user_id': '1840e0b9d4', 'category': 'Продукты'}
print(type(data))
print(json.dumps(data))
print(type(json.dumps(data)))