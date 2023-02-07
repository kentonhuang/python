STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
from dotenv import load_dotenv
import os
from twilio.rest import Client

import requests

load_dotenv("C:/Users/huang/PycharmProjects/EnvironmentVariables/.env")

alpha_key = os.getenv("ALPHA_KEY")
account_sid = os.getenv("TWILIO_SID")
auth_token = os.getenv('TWILIO_AUTH')
news_key = os.getenv("NEWS_KEY")

STOCK_NAME = "TSLA"

client = Client(account_sid, auth_token)

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
Alpha_ENDPOINT = 'https://www.alphavantage.co/query'

alpha_params = {
    "apikey": alpha_key,
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": {STOCK_NAME},
}

response = requests.get(Alpha_ENDPOINT, params=alpha_params)

data = response.json()["Time Series (Daily)"]

data_list = list(data.values())[:2]

today_close = float(data_list[0]["4. close"])

yesterday_close = float(data_list[1]["4. close"])

difference = yesterday_close - today_close

up_down = None

if difference > 0:
    up_down = "🔺"
else:
    up_down = "🔻"

diff_percent = round((difference / yesterday_close) * 100)

News_ENDPOINT = 'https://newsapi.org/v2/everything'
news_params = {
    "apiKey": news_key,
    "pageSize": 3,
    "q": {STOCK_NAME}
}

if abs(diff_percent) >= 1:
    news_response = requests.get(News_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"][:3]

    formatted_articles = [f"{STOCK_NAME}: {up_down}{diff_percent}%\nHeadline: {article['title']}. \n Brief: {article['description']}" for article in articles]

    print(formatted_articles)

    for article in formatted_articles:
        message = client.messages.create(
            body=article,
            from_='+18665167229',
            to='+14154256678'
        )

else:
    print("Less than 5% change")


## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.




## STEP 3: Use https://www.twilio.com
# Send a seperate message with the percentage change and each article's title and description to your phone number. 


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

