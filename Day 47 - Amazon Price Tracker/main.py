import requests
from bs4 import BeautifulSoup
import smtplib

AMAZON_URL = "https://www.amazon.com/Health-Home-Multifunction-Nonstick-Interchangeable/dp/B0894JVNK7/?th=1"
# HTTP HEADER
ACCEPT_LANGUAGE = "en-US,en;q=0.9"
USER_AGENT = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) " \
             "Chrome/110.0.0.0 Safari/537.36"

# SMTP email
my_email = "addison74@ethereal.email"
password = "GpynCyHfXnUmnPfXAb"

response = requests.get(AMAZON_URL, headers={'Accept-Language': ACCEPT_LANGUAGE, 'User-Agent': USER_AGENT})
website_html = response.text
# print(website_html)

soup = BeautifulSoup(website_html, "html.parser")
# print(soup.prettify())

price = float(soup.find(class_="a-offscreen").getText().strip("$"))
print(price)

title = soup.find(id="productTitle").getText().strip()
print(title)

# Send an email if price is lower than the target price
target_buy_price = 10
if price < target_buy_price:
    with smtplib.SMTP("smtp.ethereal.email", 587) as connection:
        connection.starttls()
        connection.login(user=my_email,password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs=my_email,
            msg=f"Subject:AMAZON LOW PRICE ALERT\n\n{title} is now at ${price}\n{AMAZON_URL}"
        )

