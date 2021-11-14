import praw
import pandas as pd
import json
import pprint
from datetime import datetime
import sys

def web_scrape():
    # #create reddit client
    # reddit = praw.Reddit(client_id='',  # Put the string under "personal use script" here
    #                      client_secret='',  # Put the secret here
    #                      user_agent='',  # Put the name of your app here
    #                      username='',  # Put your reddit username here
    #                      password='')  # Put your reddit password here

    #create new reddit client
    reddit = praw.Reddit("technica");
    try:
        top_posts = reddit.front.hot(limit=100)

    # If we pass in an invalid subreddit name like asjhasdasdiugqwdb, we want to handle that error appropriately
    except:
        sys.exit("Please confirm that all subreddit names are valid. ")

    # Create a dictionary to store data
    reddit_dict = {"title": [],
                   "score": [],
                   "body": [],
                   "subreddit": [],
                   "user_reports": []}

    # Iterate through the top homepage posts and append to the dictionary
    for submission in top_posts:
        reddit_dict["title"].append(submission.title)
        reddit_dict["score"].append(submission.score)
        reddit_dict["body"].append(submission.selftext)
        reddit_dict["subreddit"].append(submission.subreddit_name_prefixed)
        reddit_dict["user_reports"].append(submission.user_reports)


    reddit_data = pd.DataFrame(reddit_dict)
    reddit_data.head()

    # Convert the dataframe back to a dictionary for rapid exporting to JSON
    reddit_dict = reddit_data.to_dict('records')
    with open("home_page2.json", 'w+') as f:
        json.dump(reddit_dict, f)

