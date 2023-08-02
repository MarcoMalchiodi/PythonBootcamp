from bs4 import BeautifulSoup
import requests

data = requests.get('https://news.ycombinator.com/')
webpage = data.text

soup = BeautifulSoup(webpage, 'html.parser')

titles = []
links = []
article_titles = soup.find_all(name='a',rel='noreferrer')
for item in article_titles:
    titles.append(item.getText())
    links.append(item.get('href'))

upvotes = []
article_upvotes = soup.find_all(name="span",class_='score')
for vote in article_upvotes:
    upvotes.append(vote.getText().split()[0])


posts = []

for x in range(len(titles)):
    new_dict = {
        'title':titles[x-1],
        'upvotes':upvotes[x-1],
        'link':links[x-1]
    }
    posts.append(new_dict)




    
    


