import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇


website = requests.get(URL)
webpage = website.text

soup=BeautifulSoup(webpage, 'html.parser')

titles = soup.find_all(name="h3", class_="title")
title_list = []
for item in titles:
    title_list.append(item.getText()+"\n")

with open('mymovies.txt','w', encoding="utf8") as file:
    for title in reversed(title_list):
        file.write(title)