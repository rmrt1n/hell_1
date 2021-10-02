import json
import csv
import os

data = []
with open('data.json') as f:
    data = json.load(f)

data = [i for j in data for i in j['results']]
necessary = [dict((j, i[j]) for j in ['id', 'title', 'poster_path', 'popularity', 'vote_count', 'vote_average']) for i in data]

clean = [i for i in necessary if i['poster_path'] is not None]
#  for i, j in enumerate(clean):
    #  clean[i]['poster_path'] = 'images' + j['poster_path']

headers = clean[0].keys()
with open('processed.csv', 'w') as f:
    dict_writer = csv.DictWriter(f, headers)
    dict_writer.writeheader()
    dict_writer.writerows(clean)
