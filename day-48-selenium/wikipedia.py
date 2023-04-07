from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

service = Service("C:\development\chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://en.wikipedia.org/wiki/Main_Page")
statistics = driver.find_element(By.ID, "articlecount")
count = statistics.find_element(By.TAG_NAME, "a").text

print(count)

driver.quit()