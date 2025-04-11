import requests
import os
from twilio.rest import Client
from dotenv import load_dotenv
import html

load_dotenv()  # Load variables from .env into the environment

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"
percentage_change = 6

account_sid = os.getenv("ACCOUNT_SID")

auth_token = os.getenv("AUTH_TOKEN")

stock_params = {
    "function" : "TIME_SERIES_DAILY",
    "symbol" : STOCK_NAME,
    "apikey" : os.getenv("API_KEY_STOCK"),
}

news_params = {
    "q" : COMPANY_NAME,
    "from" : "2025-3-10",
    "sortBy" : "publishedAt",
    "apikey" : os.getenv("API_KEY_NEWS")
}

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

response = requests.get(STOCK_ENDPOINT, params=stock_params)
response.raise_for_status()
data = response.json()
print(data)
#stock_prices = response.json()["Time Series (Daily)"]
#stock_Price_today = list(stock_prices.values())[0]["1. open"]
#stock_Price_yesterday = list(stock_prices.values())[1]["1. open"]
#
#
#print(stock_Price_today)
#print(stock_Price_yesterday)

#change_in_price= stock_Price_today - stock_Price_yesterday
#percentage_change = (change_in_price * 100)/stock_Price_yesterday
if percentage_change > 0:
    up_down = "🔺"
else:
    up_down = "🔻"


response_news = requests.get(NEWS_ENDPOINT, news_params)
response_news.raise_for_status()

if abs(percentage_change) > 1:
    
    for index in range(1,2):        #range should be from (1,4) but it will costs extra on twilio every time you test
        news = response_news.json()["articles"][index]
        headline = html.unescape(news["title"])
        breif = html.unescape(news["description"])
        message_body = f"Tesla {up_down}{percentage_change}% \nHeadline:{headline}\n"
        #print(headline)
        #print(breif)
        #client = Client(account_sid, auth_token)
        #message = client.messages.create(
        #    body=message_body,
        #    from_=os.getenv("TWILIO_MOBILE_NUMBER"),
        #    to=os.getenv("VERIFIED_REAL_NUMBER")
        #)
        #print(message.status)
        #body=f"Tesla 🔺{percentage_change}% \nHeadline:{headline}\nBrief:{breif}"
        #print(body)


"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

