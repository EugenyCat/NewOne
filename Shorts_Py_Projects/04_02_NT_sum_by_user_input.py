"""
Successively queries the user numbers (one at a time)
and after the first zero return the sum of all previously entered numbers.
"""

def sum_user_number():
    """calculate sum from user's number until nuber isn't equal 0"""
    user_num = 1
    res_sum = 0
    while user_num != 0:
        print('Input number, please(for stop input 0): ', end ='')
        user_num = int(input())
        res_sum += user_num
    print(res_sum)

sum_user_number()