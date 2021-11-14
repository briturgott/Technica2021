import pandas as pd
import json
import streamlit as st

padding = 0
st.markdown(f""" <style>
    .reportview-container .main .block-container{{
        padding-top: {padding}rem;
        padding-right: {padding}rem;
        padding-left: {padding}rem;
        padding-bottom: {padding}rem;
    }} </style> """, unsafe_allow_html=True)

st.title("Welcome to Sage Social!")

st.write("Here is your Reddit profile. You can see what posts you have recently seen, and their positivity score.")

post_list = open('worldnews_subreddit.json')

if st.button('Update'):
    st.error('Updated! Make sure to refresh.')

data = json.load(post_list)

curated_post_list = []
for post in data:
    curated_post = {}
    curated_post["Title"] = post["title"]
    curated_post["Subreddit"] = post["subreddit"]
    curated_post["Username"] = post["author"]
    #new_post["Positivity"] = post["compound"] #this is where we add the scores
    curated_post_list.append(curated_post)

pretty_data = pd.DataFrame(curated_post_list)

st.dataframe(pretty_data.assign(pretty_data='').set_index('pretty_data'), width=1024, height=1024)

post_list.close()