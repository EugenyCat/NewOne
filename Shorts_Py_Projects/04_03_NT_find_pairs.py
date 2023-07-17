"""
The hypothesis is that the best recommendations we can get are simply by sorting names alphabetically
and introducing people to the same indices after sorting!
But we’re not going to introduce anyone if someone can be single:
"""

def to_find_pairs(boys:list, girls:list) -> tuple:
    """Creat pair for each boy and girl by ABC sort. If someone doesn't have pair - anybody doesn't have pair"""
    if len(boys) != len(girls):
        return ()
    else:
        boys.sort()
        girls.sort()
        return zip(boys, girls)

def print_good_pair(boys:list, girls:list) -> None:
    good_pairs = list(to_find_pairs(boys, girls))
    if len(good_pairs) == 0:
        print('\nWatch out! Someone doesn\'t have pair')
    else:
        print('\nThe best pairs:')
        for item in good_pairs:
            print(f'{item[0]} and {item[1]}')

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
print_good_pair(boys, girls)

boys = ['Peter', 'Alex', 'John', 'Arthur', 'Richard', 'Michael']
girls = ['Kate', 'Liza', 'Kira', 'Emma', 'Trisha']
print_good_pair(boys, girls)