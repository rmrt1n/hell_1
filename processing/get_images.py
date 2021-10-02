import json
import requests
import time

data = []
with open('data.json') as f:
    data = json.load(f)

data = [i for j in data for i in j['results']]
imgs = [i['poster_path'] for i in data]

#  print(imgs[535])

for i, j in enumerate(imgs[7500:]):
    print('downloading poster #{}'.format(i + 7500))
    #  time.sleep(.5)

    url = 'https://image.tmdb.org/t/p/w500/{}'.format(j)
    img = requests.get(url)

    try:
        with open('images/{}'.format(j[1:]), 'wb') as f:
            f.write(img.content)
    except:
        print('can\'t get poster #{}'.format(i + 7500))
        pass
