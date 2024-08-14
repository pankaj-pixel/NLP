import re
import pandas as pd
import string


df = pd.read_csv('labeled_data.csv')
exclude =string.punctuation
# remove all punction from data set of twitter Hate Speech and Offensive tweets
def remove_punc(text):
    return text.translate(str.maketrans('','',exclude))



tweets = df['tweet'].apply(remove_punc)
print(tweets)

