from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.python.org/')

searchbar = driver.find_element(By.NAME,'q')
searchbar_size = searchbar.size

#to find an element within an element we use the same str
driver.find_element(By.CSS_SELECTOR,'.documentation-widget a') #we are lloking for an anchor tag inside a .doc class


#If all else fails, we can always use the X path
bug_link = driver.find_element(By.XPATH, '//*[@id="site-map"]/div[2]/div/ul/li[3]/a')
print(bug_link.text)


#the find_elements simply finds everything that matches the cirteria and returns it as a list


#when there are types, values etc. inside the same line
#(By.CSS_SELECTOR, "input[type='ok'][value='myselect']")

driver.quit()