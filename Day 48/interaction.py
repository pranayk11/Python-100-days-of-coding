from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

chrome_driver_path = Service("C:\Chrome Driver\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)


driver.get("https://en.wikipedia.org/wiki/Main_Page")

no_of_articles = driver.find_element(by=By.CSS_SELECTOR, value="#articlecount a")
# print(no_of_articles.text)
# no_of_articles.click()

# Automate form filling
search = driver.find_element(by=By.NAME, value="search")
search.send_keys("Python")
search.send_keys(Keys.ENTER)

time.sleep(10)
driver.quit()
