import urllib.request, json
from warnings import catch_warnings
import numpy as np 
import pandas as pd
from pandas import json_normalize
import io

def get_submission_data(handles):
    vals = []
    for handle in handles:
        path = "https://codeforces.com/api/user.status?handle=" + str(handle) + "&from=1&count=3000"
        print(path) 
        with urllib.request.urlopen(path) as url:
            data = json.loads(url.read().decode())
            df = pd.DataFrame(json_normalize(data))
            for z in df['result'][0]:
                if 'rating' not in z['problem'] or z['verdict'] != 'OK':
                    continue
                vals.append((z['problem']['rating'], z['problem']['name']))
            
    F = [0] * 100
    for x, y in set(vals):
        F[int(x / 100)] += 1

    return F[15:27]

# data = get_submission_data(['mh755628', '00000007', 'I_HATE_GEOMETRY'])

data = [70, 68, 78, 91, 151, 143, 134, 129, 118, 115, 103, 47]

#make a bar chart of the data wide

col = []

for x in data:
    if x >= 100:
        col.append('green')
    elif x >= 80:
        col.append('yellow')
    elif x >= 50:
        col.append('orange')
    else:
        col.append('red')

import matplotlib.pyplot as plt

rating = []
for i in range(len(data)):
    rating.append((i + 15) * 100)
y_pos = np.arange(len(data))
plt.bar(y_pos, data, align='center', alpha=0.5, color = col)
plt.xticks(y_pos, rating)
plt.grid(alpha=0.7)
plt.show()
