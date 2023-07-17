import pickle
import os

"""---1---"""
"""Pickle example"""
data = {'user_id': '1840e0b9d4', 'category': 'Products'}

with open('files/data.pickle', 'wb') as f:
    pickle.dump(data, f)


"""Read pickle file"""
with open('files/data.pickle', 'rb') as f:
    dict_ = pickle.load(f)

print(dict_, dict_['user_id'])


"""---2---"""
"""OS example"""
"""Read files from repository"""
for file in os.listdir('files'):
    if '.csv' in file:
        print(file)


"""Read all files and repositories"""
for root, directory, file in os.walk('files'):
    print(root, directory, file)