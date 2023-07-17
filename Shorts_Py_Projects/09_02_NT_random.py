"""
Write the code that will generate a random sequence of 6 digits, one of which should be 3.
The position of the digit 3 should be determined at random. The result should be a string.
For example: "456309" or "330127".
"""

import random

int_nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

pos_three = random.randint(0, 5)
print(f'Position number three in sequence: {pos_three+1}')

sequence = random.sample(int_nums, 6)

while sequence[0] == 0:
    sequence = random.sample(int_nums, 6)

sequence[pos_three] = 3
print('Result sequence: ', end='')
print(*sequence, sep='')