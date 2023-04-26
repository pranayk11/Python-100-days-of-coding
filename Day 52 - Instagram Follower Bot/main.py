from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.common.exceptions import ElementClickInterceptedException
import time

chrome_driver_path = Service("C:\Chrome Driver\chromedriver.exe")

INSTAGRAM_URL = "https://www.instagram.com/"
USERNAME = "username"
PASSWORD = "password"
TARGET_ACCOUNT = "account you want to target"


class InstaFollower:
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_driver_path)

    def login(self):
        self.driver.get(INSTAGRAM_URL)
        time.sleep(10)
        username = self.driver.find_element(By.NAME, "username")
        time.sleep(10)
        username.send_keys(USERNAME)

        password = self.driver.find_element(By.NAME, "password")
        time.sleep(10)
        password.send_keys(PASSWORD)

        login = self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]/button')
        login.click()
        time.sleep(15)

    def find_followers(self):
        self.driver.get(f"https://www.instagram.com/{TARGET_ACCOUNT}/")
        time.sleep(10)
        followers = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div[2]/section/main/div/header/section/ul/li[2]/a/div')
        followers.click()
        time.sleep(5)

    def follow(self):
        follow_btn = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")

        for follow in follow_btn:
            try:
                follow.click()
                time.sleep(3)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower()
bot.login()
bot.find_followers()
bot.follow()
