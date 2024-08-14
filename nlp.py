import re
import string
import pandas as pd
from textblob import  TextBlob
from nltk.corpus import stopwords
import nltk
#nltk.download('stopwords')








text ="""
<h1>The Future of Artificial Intelligence</h1>
<p>Artificial Intelligence (AI) is revolutionizing the way we live and work.
 From <a href="https://example.com/healthcare">healthcare</a> to <a href="https://example.com/finance">finance</a>,
 AI-driven solutions are transforming industries. Machine learning algorithms can analyze vast amounts of data to identify patterns, make predictions, and improve decision-making processes.
 As AI continues to advance, ethical considerations and regulations will play a crucial role in guiding its development.
 Learn more about AI in <a href="https://example.com/ai-ethics">AI ethics</a> and its impact on society.</p>
"""
#step1 is to lower casing the text scraped from websites
data = text.lower()
#print(data)  



# Step2 remove all html tags from data using regular expression
def remove_html_tags(text):
    pattern =re.compile('<.*?>')
    return pattern.sub(r'',text)
result = remove_html_tags(text)
#print(result)


#step 3 remove  url if any
text1 = "https://stackoverflow.com/questions/21932615/regular-expression-for-remove-link pankaj its You??"
text2 ="http://Internet URL goes here."
text3 = "https://www.youtube.com/watch?v=29qyNyNkLHs Developer 11"

def remove_url(text1):
    pattern = re.compile('https?://\S+|www\.\S+')
    return pattern.sub(r'',text3)
results1 =remove_url(text3)
#print(results1)



#step 4 Remove Punctuation
punc_word = string.punctuation
#print(punc_word)
txt ="my name is Pankaj. do you know! why???? ok got it !"
def remove_punc(txt):
    return txt.translate(str.maketrans('','',punc_word))

#res = remove_punc(txt)
#print(res)





# step5 chat word treatment
# likse ASAP => as soon as possible
slangWords = pd.read_csv('slang.csv')

slang = slangWords['acronym']
actual = slangWords['expansion']

words = slangWords.set_index('acronym')['expansion'].to_dict()
#print(words)


def chat_converstion(user_word):
    new_text =[]
    for w in user_word.split():
        if w in words:
            new_text.append(words[w])
        else:
            new_text.append(w)
    return " ".join(new_text)            

#result = chat_converstion('2nite')
#print(result)







#step 6 spelling checker
#use textblob

incorrect_spelling = " thhis is your boi how are you deing I am good what ebout you"
#print("InCorrect : ",incorrect_spelling)

textblb = TextBlob(incorrect_spelling)
res = textblb.correct().string
#print("Correct : ",res)




#step 7 nltk for removing stop words

paragraph = [""" In conclusion, creating a dictionary from two Pandas DataFrame columns can be achieved through various methods,
including using the zip function, and the to_dict method.
The choice of method depends on the specific requirements of your task and the structure of your data."""]

stopwords.words('english')


def stop_words(paragraph):
    new_tex = []
    for i in paragraph:
        if i in stopwords.words('english'):
            new_tex.append(' ')
        else:
            new_tex.append(i)
    return " ".join(new_tex)

obj1 =  stop_words(paragraph)
print(obj1)





