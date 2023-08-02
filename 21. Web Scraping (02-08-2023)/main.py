from bs4 import BeautifulSoup

with open('website.html', encoding="utf8") as file:
    contents = file.read()

soup=BeautifulSoup(contents, "html.parser") #the second element is the parser: the language we want to read the file with
#print(soup.h1)
#soup.h1.name returns the name of that particular tag
#print(soup.beautify()) prints the indented html file
#print(soup.li)

all_anchortags = soup.find_all(name='a') #will return all a tags as a list

for tag in all_anchortags:    
   # print(tag.getText()) will print the content of each row
   # print(tag.get("href")) will print the href (in this case a link)
   pass

heading = soup.find(name="h1",id="name")
# print(heading.getText())

#name > returns the tag's name
#getText() > returns the text content
#get("insert value") > returns a specific value
#find_all() > returns all elements with that tag/value

company_url = soup.select_one(selector="p a") #"p a" is an a tag inside a p tag

headings = soup.select(".heading") #returns a list with all class="heading"