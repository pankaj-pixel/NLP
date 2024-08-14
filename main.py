from bs4 import BeautifulSoup
import requests
import lxml

url = "https://www.brightorangethread.com/blog/view/50-is-the-magic-number-of-blog-posts-for-your-company"

response = requests.get(url)
#print(response.status_code)

raw = response.text
soup = BeautifulSoup(raw ,"lxml")


Articles = soup.find('article',class_="article")
paragraph = Articles.find_all('p')[4]
data = paragraph
print(data.text)
#step 1 convert the text into lower case
print(data.lower())
