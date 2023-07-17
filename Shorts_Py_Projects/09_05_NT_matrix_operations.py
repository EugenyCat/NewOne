"""
1.  Print the result of adding all elements of the matrix.
2.  Write an algorithm for calculating the maximum of the sum of the elements of each column.
"""

matrix = [
    [0,1,2,4,8],
    [6,2,2,1,9],
    [3,3,3,3,3],
    [4,6,7,1,2],
    [5,7,3,4,0],
    [5,7,3,4,0]
]


def sum_of_elements_matrix(double_matrix: list) -> int:
    sum_el_matrix = 0
    for x in double_matrix:
        for y in x:
            sum_el_matrix += y
    return sum_el_matrix


def max_sum_or_column(double_matrix: list) -> int:
    max_sum_el_matrix = double_matrix[0][0]
    num_of_max_column = 0
    for y in range(len(double_matrix[0])):
        column_sum = 0
        for x in range(len(double_matrix)):
            column_sum += double_matrix[x][y]
        if column_sum > max_sum_el_matrix:
            num_of_max_column = y
            max_sum_el_matrix = column_sum
    print(f'Num of max column: {num_of_max_column}')
    return max_sum_el_matrix


print(sum_of_elements_matrix(matrix))
print(max_sum_or_column(matrix))