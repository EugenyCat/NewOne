import pandas as pd
import re

"""
For the log.csv create the column source_type according to the rules:

if the source traffic_source is Yandex or Google, the source_type is organic;
for paid and email sources from Russia put ad;
for paid and email sources not from Russia put other;
all other options take from traffic_source unchanged.
"""


def calc_source_type(row):
    source_type = None
    if re.search('yandex|google', row.traffic_source):
        source_type = 'organic'
    elif re.search('paid|email', row.traffic_source):
        if row.region == 'russia':
            source_type = 'ad'
        else:
            source_type = 'other'
    else:
        source_type = row.traffic_source
    return source_type


log = pd.read_csv('datasets/visit_log.csv', sep=';')

log['source_type'] = log.apply(calc_source_type, axis=1)

print(log[['source_type', 'traffic_source', 'region']])