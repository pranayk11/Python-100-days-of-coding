from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("C:\Chrome Driver\chromedriver.exe")


TWITTER_URL = "https://twitter.com/i/flow/login"
TWITTER_EMAIL = "your email"
TWITTER_PASSWORD = "password"
TWITTER_USERNAME = "your username"
PROMISED_UP = 7
PROMISED_DOWN = 10
SPEED_TEST_URL = "https://www.speedtest.net/"


class InternetSpeedTwitterBot:
    def __init__(self):
        self.driver = webdriver.Chrome(service=chrome_driver_path)
        self.down = 0
        self.up = 0

    def get_internet_speed(self):
        self.driver.get(SPEED_TEST_URL)
        go_btn = self.driver.find_element(by=By.CLASS_NAME, value="start-text")
        go_btn.click()
        time.sleep(50)

        self.down = float(self.driver.find_element(by=By.CLASS_NAME, value="download-speed").text)

        self.up = float(self.driver.find_element(by=By.CLASS_NAME, value="upload-speed").text)

    def tweet_at_provider(self):
        if self.down < PROMISED_DOWN:
            self.driver.get(TWITTER_URL)
            time.sleep(15)
            log_in = self.driver.find_element(by=By.TAG_NAME, value="input")
            time.sleep(10)
            log_in.send_keys(TWITTER_EMAIL)
            time.sleep(5)

            next_btn1 = self.driver.find_element(by=By.XPATH, value='//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div/span/span')
            next_btn1.click()
            time.sleep(10)

            # If suspicious activity detected
            username = self.driver.find_element(by=By.TAG_NAME, value="input")
            username.send_keys(TWITTER_USERNAME)
            time.sleep(5)
            next_btn2 = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div/div/div/div/span/span')
            next_btn2.click()
            time.sleep(5)

            password = self.driver.find_element(By.NAME, "password")
            time.sleep(5)
            password.send_keys(TWITTER_PASSWORD)

            login_btn = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span')
            time.sleep(5)
            login_btn.click()
            time.sleep(10)

            # Write tweet
            self.driver.find_element(By.CSS_SELECTOR, 'a[aria-label="Tweet"]').click()
            write_tweet = self.driver.find_element(By.CSS_SELECTOR, 'div[data-contents="true"]')
            write_tweet.send_keys(f"Hi @Service provider, my internet speed is {self.down}down/{self.up}up"
                                  f"instead of promised {PROMISED_DOWN}down/{PROMISED_UP}up")
            time.sleep(2)
            self.driver.find_element(By.XPATH, '/html/body/div[1]/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div/div[3]/div[2]/div[1]/div/div/div/div/div[2]/div[3]/div/div/div[2]/div[4]').click()
            time.sleep(10)


bot = InternetSpeedTwitterBot()
bot.get_internet_speed()
bot.tweet_at_provider()

