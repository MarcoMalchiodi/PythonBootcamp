#automatic log-in
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

email='fakeemailaddress@studenti.unimi.it'
password='NOTAPASSWORD'

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://cas.unimi.it/login?service=https%3A%2F%2Funimia.unimi.it%2Fportal%2Fserver.pt%2Fcommunity%2Funimia%2F207')

username = driver.find_element(By.NAME,'username')
username.send_keys(email)

insert_pass = driver.find_element(By.NAME,'password')
insert_pass.send_keys(password)

accedi = driver.find_element(By.CSS_SELECTOR, "input[type='submit'][value='Accedi']")
accedi.send_keys(Keys.ENTER)

driver.quit()
