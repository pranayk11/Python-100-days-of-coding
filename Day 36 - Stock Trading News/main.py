import requests
from twilio.rest import Client
import os

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
STOCK_API_KEY = os.environ["STOCK_API_KEY"]
NEWS_API_KEY = os.environ['NEWS_API_KEY']

# Twilio
# twilio_failsafe = "Jp1elj5X0_Pa_pK90fIzyfFXH_oNEVsK9cwWceb4"
account_sid = os.environ["Twilio_account_sid"]
auth_token = os.environ['Twilio_auth_token']

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

stock_parameter = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "apikey": STOCK_API_KEY,
    "symbol": STOCK,
}

news_parameter = {
    "q": COMPANY_NAME,
    "from": "2023-03-01",
    "sortBy": "popularity",
    "apikey": NEWS_API_KEY
}


## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

stock_response = requests.get(url=STOCK_ENDPOINT, params=stock_parameter)
stock_response.raise_for_status()
stock_data = stock_response.json()

yesterday = stock_data["Time Series (Daily)"]["2023-03-01"]
yesterday_closing = float(yesterday["4. close"])
# print(yesterday_closing)

before_yesterday = stock_data["Time Series (Daily)"]["2023-02-28"]
before_yesterday_closing = float(before_yesterday["4. close"])
# print(before_yesterday_closing)

# Percentage Change
price_diff = yesterday_closing - before_yesterday_closing
percent_change = round((price_diff/before_yesterday_closing) * 100)
print(percent_change)

# Get news if stock price decrease/increase by -5/+5 %
if percent_change > 5 or percent_change < -5:
    news_response = requests.get(url=NEWS_ENDPOINT, params=news_parameter)
    news_response.raise_for_status()
    news_data = news_response.json()

    news = [new_news for new_news in news_data["articles"][:3]]
    news_body = ""
    for msg in news:
        news_body += "".join(f"Headline:{msg['title']}\n"
                             f"Brief:{msg['description']}\n\n")

    if price_diff > 0:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK}: 🔺{percent_change}%\n{news_body}",
            from_="+447700158508",
            to="+447700184864"
        )
        print(message.status)
    elif price_diff < 0:
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK}: 🔻{percent_change}%\n{news_body}",
            from_="+447700158508",
            to="+447700184864"
        )
        print(message.status)
else:
    print("There was no significant change in the stock price.")


#Optional: Format the SMS message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

