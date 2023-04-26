import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

GOOGLE_FORM_URL = "https://docs.google.com/forms/d/e/1FAIpQLSfgHSObxpECT4bQSvQyMpCQUUdE2lQarksbnf2qt1vaA-gJvQ/viewform?usp=sf_link"
ZILLOW_URL = "https://www.zillow.com/san-francisco-ca/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22mapBounds%22%3A%7B%22north%22%3A37.908143094647194%2C%22east%22%3A-122.22184268359375%2C%22south%22%3A37.64220165564354%2C%22west%22%3A-122.64481631640625%7D%2C%22mapZoom%22%3A11%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22price%22%3A%7B%22max%22%3A872627%7D%2C%22beds%22%3A%7B%22min%22%3A1%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22mp%22%3A%7B%22max%22%3A3000%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22fsba%22%3A%7B%22value%22%3Afalse%7D%7D%2C%22isListVisible%22%3Atrue%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A20330%2C%22regionType%22%3A6%7D%5D%7D"

# MY HTTP HEADER
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/111.0.0.0 Safari/537.36"
ACCEPT_LANGUAGE = "en-US,en;q=0.9"

# # SCARPING USING BEAUTIFUL-SOUP

response = requests.get(ZILLOW_URL, headers={"Accept-Language": ACCEPT_LANGUAGE, "User-Agent": USER_AGENT})
website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")
# print(soup)


# Address from listings in Zillow
address_list = soup.find_all(name="address")
all_address = [address.getText() for address in address_list]
# print(address)

# Prices from listings in Zillow
price_list = soup.select(selector=".bqsBln span")
all_price = [price.getText().split("+")[0].split("/mo")[0] for price in price_list]
# print(price)

# Property link from listings in Zillow
all_links = []
link_list = soup.find_all(name="a", class_="property-card-link")
for link in link_list:
    link = link.get("href")
    if "http" not in link:
        all_links.append(f"https://www.zillow.com{link}")
    else:
        all_links.append(link)
# print(all_links)


# AUTOMATION USING SELENIUM

chrome_driver_path = Service("C:\Chrome Driver\chromedriver.exe")

driver = webdriver.Chrome(service=chrome_driver_path)
driver.maximize_window()

for n in range(len(all_address)):
    driver.get(GOOGLE_FORM_URL)
    time.sleep(5)

    address = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')
    price = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
    link = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
    submit = driver.find_element(By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')

    address.send_keys(all_address[n])
    price.send_keys(all_price[n])
    link.send_keys(all_links[n])
    time.sleep(2)
    driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)  # Scroll page down
    time.sleep(2)
    submit.click()
