which nltk
import json
import pandas as pd

analyzer = SIA()

post_list = open('post_text.json')
data = json.load(post_list)

for i in data:
    pol = analyzer.polarity_scores(i['title'])

post_list.close()