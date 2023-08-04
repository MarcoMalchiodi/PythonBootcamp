#create a dictionary containing all upcoming events
from selenium import webdriver
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
driver.get('https://www.python.org/')

dates = []
events_date = driver.find_elements(By.CSS_SELECTOR,'.medium-widget.event-widget.last .shrubbery ul li time')
for item in events_date:
    try: 
        dates.append(item.text)
    except:
        pass

events = []
events_name = driver.find_elements(By.CSS_SELECTOR,'.medium-widget.event-widget.last .shrubbery ul li a')
for item in events_name:
    try: 
        events.append(item.text)
    except:
        pass

upcoming_events= {}
    
for x in range(len(events)):
    upcoming_events[x]={
        'time':dates[x-1],
        'event':events[x-1]
    }

print(upcoming_events)



driver.quit()