from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

# driver.get("https://www.amazon.com/fire-tv-stick-4k-max-with-alexa-voice-remote/dp/B08MQZXN1X?th=1")
#
# price = driver.find_element(By.CLASS_NAME, "a-offscreen")
# print(price.get_attribute('innerHTML'))

driver.get("https://www.python.org/")
event_widget = driver.find_element(By.CLASS_NAME, "event-widget")
events = event_widget.find_elements(By.TAG_NAME, "li")

events_dict = {}

for n in range(len(events)):
    time = events[n].find_element(By.TAG_NAME, "time").text
    event_name = events[n].find_element(By.TAG_NAME, "a").text

    events_dict[n] = {
        "time": time,
        "name": event_name
    }

print(events_dict)

# driver.close()
driver.quit()