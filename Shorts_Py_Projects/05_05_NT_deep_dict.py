"""
It is necessary to write the code, which on the basis of the original list
will make a dictionary of this level of nesting, what is the length of the original list.
"""

def create_ultra_deep_dict(in_list:list, index:int=0) -> dict:
    """Example recursion. Create dictionary from list, where each next element is key of next dictionary"""
    dict_template = { }
    if index == len(in_list)-1:
        dict_template[in_list[index - 1]] = in_list[index]
    else:
        index += 1
        dict_template[in_list[index - 1]] = create_ultra_deep_dict(in_list, index)
    return dict_template


my_list = ['2018-01-01', 'yandex', 'cpc', 100]
#my_list = ['a', 'b', 'c', 'd', 'e', 'f']
print(create_ultra_deep_dict(my_list))