import datetime
import json
import os
import requests
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
red_triangle = "🔺"
inverted_red_triangle = "🔻"
# get yesterday date
yesterday = (datetime.date.today() - datetime.timedelta(days=3)).strftime("%Y-%m-%d")
day_before_yesterday = (datetime.date.today() - datetime.timedelta(days=4)).strftime("%Y-%m-%d")

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 2% between yesterday and the day before yesterday then print("Get News").

account_sid = os.environ.get('ACCOUNT_SID')
auth_token = os.environ.get('AUTH_TOKEN_TWILIO')

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "api",
}
news_parameters = {
    "function": "NEWS_SENTIMENT",
    "symbol": STOCK,
    "apikey": "api",

}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()
news_response  = requests.get(STOCK_ENDPOINT,params=news_parameters)
news_data = news_response.json()

yesterday_closing_price = data["Time Series (Daily)"][yesterday]["1. open"]
day_before_yesterday_price = data["Time Series (Daily)"][day_before_yesterday]["4. close"]

# Calculate the diference between yesterday_closing_price and day_before_yesterday_price in %
def calculate_difference():
    percentage_difference = ((float(yesterday_closing_price) - float(day_before_yesterday_price)) / float(day_before_yesterday_price)) * 100
    if percentage_difference > 2:
        get_news(red_triangle, percentage_difference)
    elif percentage_difference < -2:
        get_news(inverted_red_triangle, percentage_difference)
    else:
        print("No News")
        get_news(inverted_red_triangle, percentage_difference)

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 

def get_news(triangle,difference):
    news_title = news_data['feed'][0]['title']
    news_summary = news_data['feed'][0]['url']
    body_message = str(f'{COMPANY_NAME}: {triangle}{difference:.2f}%\nHeadline: {news_title}\nBrief: {news_summary[:150]}')
    client = Client(account_sid, auth_token)
    message = client.messages.create(
            from_='+13312461663',
            body=body_message,
            to='+50660437458'
        )
    print(message.sid,body_message)  


calculate_difference()