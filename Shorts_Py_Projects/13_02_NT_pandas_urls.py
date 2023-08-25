import pandas as pd
from urllib.parse import urlparse

"""
The URLs.txt file contains the URL of the news site pages. You need to filter it to the addresses of the news pages. 
It is known that the news page template has inside: the URL template /website/, then 8 digits, then a hyphen.
"""


urls = pd.read_csv('datasets/URLs.txt')
urls = urls[urls.url.str.contains('\/[a-z]+\/\d+-', regex=True)]
print(urls.head())