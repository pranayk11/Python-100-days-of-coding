from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

AMAZON_URL = "https://www.amazon.in/gp/product/B0BSNQ2KXF/ref=s9_acss_bw_cg_Budget_8a1_w?pf_rd_m=A1K21FY43GMZF8&pf_rd_s=merchandised-search-11&pf_rd_r=QV2R2Z6XT4XPCXW8Y3K7&pf_rd_t=101&pf_rd_p=f5949445-c9a2-4600-b751-eb5de3396d69&pf_rd_i=1389401031&th=1"
chrome_driver_path = Service("C:\Chrome Driver\chromedriver.exe")
driver = webdriver.Chrome(service=chrome_driver_path)

# driver.get(AMAZON_URL)
# price = driver.find_element(by=By.CLASS_NAME, value="a-offscreen").get_attribute("textContent").strip("₹")
# price = float(price.replace(",", ""))
# print(price)

driver.get("https://python.org")
event_time = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget time")
event_name = driver.find_elements(by=By.CSS_SELECTOR, value=".event-widget li a")

event_dict = {}
for n in range(len(event_time)):
    event_dict[n] = {
        "time": event_time[n].text,
        "name": event_name[n].text
    }
print(event_dict)

# driver.close()  # Closes a single active tab
driver.quit()  # Quits the entire browser
