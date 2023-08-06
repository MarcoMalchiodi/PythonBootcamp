# ------------------- Using BS to retrieve webpage content ----------- #
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen

url='https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.902454383317135%2C%22east%22%3A-122.25136844042969%2C%22south%22%3A37.64791042690182%2C%22west%22%3A-122.61529055957031%7D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%2C%22mapZoom%22%3A11%7D'

request = Request(url, headers={'User-Agent':'Mozilla/5.0'})
webpage = urlopen(request).read()

soup=BeautifulSoup(webpage,'html.parser')

prices=[]
price_data = soup.find_all(name='span', attrs={'data-test':'property-card-price'})
for item in price_data:
    prices.append(item.text[:6])

addresses=[]
address_data = soup.find_all(name='address',attrs={'data-test':'property-card-addr'})
for item in address_data:
    addresses.append(item.text)


property_links=[]
links = soup.find_all(name='a',attrs={'data-test':'property-card-link'})
for link in links:
    property_links.append(link.get('href'))


# --------------------- Using Selenium to fill in forms ---------- #
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import ElementNotInteractableException, TimeoutException

docs_url = 'https://docs.google.com/forms/d/e/1FAIpQLSeUpJmEhUvN5QB_OCrQF4Qtu3AOhit3cyXMcnBbYCPoA7vtgQ/viewform?usp=sf_link'

for x in range(len(addresses)):

    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.get(docs_url)

    first_question=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    first_question.send_keys(addresses[x])
    
    second_question=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    second_question.send_keys(prices[x])
    
    third_question=driver.find_element(By.XPATH,'//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    third_question.send_keys(property_links[x])
    
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span')
    submit.send_keys(Keys.ENTER)


driver.quit()