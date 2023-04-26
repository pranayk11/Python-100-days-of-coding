from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import time
import random

LINKEDIN_URL = "https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&" \
               "keywords=python%20developer&location=London%2C%20England%2C%20United%20Kingdom&" \
               "redirect=false&position=1&pageNum=0"
MY_EMAIL = "hakah85671@rolenot.com"
MY_PASSWORD = "qwerty@1234"

chrome_driver_path = Service("C:\Chrome Driver\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# Open Chrome in maximised mode
driver.maximize_window()

driver.get(LINKEDIN_URL)

random_sleep = [7, 5, 10]

# Sign-in & Login in Linkedin
sign_in = driver.find_element(by=By.CLASS_NAME, value="nav__button-secondary")
time.sleep(random.choice(random_sleep))
sign_in.click()

email = driver.find_element(by=By.ID, value="username")
time.sleep(random.choice(random_sleep))
email.send_keys(MY_EMAIL)

password = driver.find_element(by=By.ID, value="password")
time.sleep(random.choice(random_sleep))
password.send_keys(MY_PASSWORD)

login = driver.find_element(by=By.CLASS_NAME, value="login__form_action_container")
time.sleep(random.choice(random_sleep))
login.click()

# Message popup minimise
time.sleep(10)
msg_min = driver.find_element(By.CLASS_NAME, "msg-overlay-bubble-header__details")
time.sleep(5)
msg_min.click()

# Jobs listings
time.sleep(10)
jobs_listings = driver.find_elements(By.CLASS_NAME, "jobs-search-results__list-item")

for job in jobs_listings:
    job.click()
    # Save Button
    time.sleep(5)
    save = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/div[1]/div/div[1]/div[1]/div[3]/div/button')
    time.sleep(10)
    save.click()
    # Scroll down to locate follow button
    time.sleep(5)
    driver.find_element(By.TAG_NAME, "html").send_keys(Keys.END)
    # Follow button
    time.sleep(3)
    try:
        follow = driver.find_element(By.XPATH, '/html/body/div[5]/div[3]/div[4]/div/div/main/div/section[2]/div/div[2]/div[1]/div/section/section/div[1]/div[1]/button')
        time.sleep(5)
        follow.click()
    except NoSuchElementException:
        pass

time.sleep(10)
driver.quit()
