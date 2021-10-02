import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv('API_KEY')

l = []
for i in range(1, 501):
    print('requesting page #{}'.format(i))

    req = 'https://api.themoviedb.org/3/discover/movie'
    req += '?api_key={}'.format(API_KEY)
    req += '&page={}'.format(i)
    req += '&include_adult=false'

    data = requests.get(req)
    l.append(data.json())

with open('data.json', 'w') as f:
    f.write(json.dumps(l, indent=2))
