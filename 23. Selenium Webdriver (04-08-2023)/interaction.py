from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://en.wikipedia.org/wiki/Main_Page')


#CLICKING
english_articles = driver.find_element(By.CSS_SELECTOR,'#articlecount a')
#click on the element
#english_articles.click()

#another method to click on a link is with find_element_link_text
source = driver.find_element(By.LINK_TEXT,'Wikipedia')
#source.click()


#TYPING
search = driver.find_element(By.NAME,'search')
search.send_keys('Python')
#if we want to return key that is not a typical str (ex. enter key) we need to import keys
#search.send_keys(Keys.ENTER)

#IF IT GOES STALE
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Wait for the search element to be available again
search = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, 'search'))
)

# Type 'Python' and press Enter
search.send_keys(Keys.ENTER)

input()
driver.quit()