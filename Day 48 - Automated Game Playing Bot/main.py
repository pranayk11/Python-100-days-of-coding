from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

chrome_driver_path = Service("C:\Chrome Driver\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on
cookie = driver.find_element(by=By.ID, value="cookie")
# Get cookie count


# Get upgrade items id
items = driver.find_elements(by=By.CSS_SELECTOR, value="#store div")
items_id = [item.get_attribute("id") for item in items]

# Get item price of the upgrade
# prices = []
# for upgrade in upgrades[:-1]:
#     upgrade_item = upgrade.text.split("-")
#     item_price = int(upgrade_item[1].replace(",", ""))
#     prices.append(item_price)
# print(prices)


five_min = time.time() + (60 * 5)  # 5 min duration
every_5_sec = time.time() + 5


# def buy_upgrade():
#     for price in prices[::-1]:
#         if money >= price:
#             return upgrades[prices.index(price)].click()


while True:
    cookie.click()
    # Every 5 seconds:
    if time.time() > every_5_sec:
        # Get all upgrade <b> tags
        all_prices = driver.find_elements(by=By.CSS_SELECTOR, value="#store b")
        item_prices = []

        # Convert <b> text into integer price
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = items_id[n]

        # Get current cookie count
        money = int(driver.find_element(by=By.ID, value="money").text.replace(",", ""))

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if money > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element(by=By.ID, value=to_purchase_id).click()
        # Add another 5 seconds until the next check
        every_5_sec = time.time() + 5

    # After 5 min stop the bot and check cookie per second count
    if time.time() > five_min:
        cookies_per_sec = driver.find_element(by=By.ID, value="cps")
        print(cookies_per_sec.text)
        break

driver.quit()
