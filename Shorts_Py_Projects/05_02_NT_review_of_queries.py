"""
Given a variable that stores a list of user search queries.
You need to write a program that will display the distribution of the number of words in queries in the desired form.
"""

def print_revue_of_queries(qrs:list) -> None:
    total_req = len(qrs)
    freq_queries = calculate_count_words_in_queries(qrs)
    for item in freq_queries:
        print(f'Search queries are containing {item} words: {round(freq_queries[item]/total_req*100, 2)}%')


def calculate_count_words_in_queries(qrs:list) -> dict:
    freq_queries = {}

    for query in qrs:
        if freq_queries.get(len(query.split(' '))) is None:
            freq_queries[len(query.split(' '))] = 1
        else:
            freq_queries[len(query.split(' '))] += 1
    return freq_queries

queries = [
    'смотреть сериалы онлайн',
    'новости спорта',
    'афиша кино',
    'курс доллара',
    'сериалы этим летом',
    'курс по питону',
    'сериалы про спорт',
]

print_revue_of_queries(queries)
