import pandas as pd
import requests
from bs4 import BeautifulSoup
"""
https://github.com/obulygin/pyda_homeworks/blob/master/web_scraping/web_scraping.ipynb
бибилиотеки
requests - для получения html
BuetufelSoup
silenium
"""

habr_head = 'https://habr.com'


def get_posts(resources:list, page_count=1):
    total_res = {'title': [], 'time': [], 'link': [], 'favorites' : [], 'text': []}

    for page in range(1, page_count+1):
        for res in resources:
            req = requests.get(f'https://habr.com/ru/search/page{page}/', params={'q': res})
            soup = BeautifulSoup(req.text, 'html.parser')


            title_list = soup.find_all('a', attrs={'data-test-id':'article-snippet-title-link'})
            for title in title_list:
                for title_contests in title.contents:
                    title_to_list = ''
                    for title_contests_descendants in title_contests.descendants:
                        if str(type(title_contests_descendants)) == "<class 'bs4.element.NavigableString'>":
                            title_to_list += str(title_contests_descendants)
                    total_res.get('title').append(title_to_list)


            time_post_list = soup.find_all('span', attrs={'class' : 'tm-article-datetime-published'})
            for span in time_post_list:
                for span_time in span.contents:
                    total_res.get('time').append(span_time['title'])


            link_list = soup.find_all('h2', attrs={'class': 'tm-title tm-title_h2'})
            for link in link_list:
                for link_contents in link.contents:
                    total_res.get('link').append(habr_head + link_contents['href'])

                    req_post = requests.get(habr_head + link_contents['href'])
                    inner_soup = BeautifulSoup(req_post.text, 'html.parser')

                    favorites_count_list = inner_soup.find_all('span', attrs={'class': 'bookmarks-button__counter'})
                    total_res.get('favorites').append(int(favorites_count_list[0].contents[0]))


                    texts_list = inner_soup.find_all('div', attrs={'class': 'article-formatted-body article-formatted-body article-formatted-body_version-2'}) \
                                 or inner_soup.find_all('div', attrs={'class': 'article-formatted-body article-formatted-body article-formatted-body_version-1'})

                    if texts_list:
                        for text_item in  texts_list:
                            for text_content in text_item.contents:
                                total_res.get('text').append(text_content.text)
                    else:
                        total_res.get('text').append('error of parsing')

    ret = pd.DataFrame.from_dict(total_res)
    return ret


print(get_posts(['python'], page_count=1).head())