from nltk.sentiment.vader import SentimentIntensityAnalyzer as SIA
import json
import pandas as pd

def analysis():
    analyzer = SIA()
    
    post_list = open('home_page2.json')
    data = json.load(post_list)
    print("hello")
    
    for i in data:
        pol = analyzer.polarity_scores(i['title'])
        i["compound"] = pol["compound"]
        print(pol)
    
    post_list.close()
    with open("home_page2.json", 'w+') as f:
        json.dump(data, f)