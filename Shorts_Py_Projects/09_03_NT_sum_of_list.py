"""
Write an algorithm that produces a number equal to the sum of the items in the list that are greater
than 10 but less than 100 and that are greater than 200 but less than 500.
"""


list_01 = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 14, 46, 273, 22, 99, 15, 1000]
list_01 = [1, 1, 2, 3, 5, 8, 13, 21]


def elements_for_sum(nums_list, m:int=0, prefix = None, start=10, finish=100):
    prefix = prefix or []
    if (m == len(nums_list)) or start < sum(prefix) < finish:
        print(prefix)
        return
    for item in nums_list[m:]:
        if sum(prefix) + item >= finish:
            continue
        else:
            prefix.append(item)
            elements_for_sum(nums_list, m+1, prefix, start, finish)
            prefix.pop()



print('Between 10 and 30')
elements_for_sum(list_01, start=10, finish=30)

print('Between 10 and 100')
#elements_for_sum(list_01)

print('Between 200 and 500')
#elements_for_sum(list_01, start=100, finish=500)