import datetime
import json
import os
import requests
from twilio.rest import Client

STOCK = "RDDT"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
red_triangle = "🔺"
inverted_red_triangle = "🔻"
# get yesterday date
yesterday = (datetime.date.today() - datetime.timedelta(days=3)).strftime("%Y-%m-%d")
day_before_yesterday = (datetime.date.today() - datetime.timedelta(days=4)).strftime("%Y-%m-%d")

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

account_sid = "AC1d9ace12d1f4b751050e6e1ff6fa0059"#os.environ.get('ACCOUNT_SID')
auth_token = "4b71ccadd5cf26ae4ce66699d53b0baf"#os.environ.get('AUTH_TOKEN_TWILIO')

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "IU0NDP82K7KQJH6B",
}
news_parameters = {
    "function": "NEWS_SENTIMENT",
    "symbol": STOCK,
    "apikey": "IU0NDP82K7KQJH6B",

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
#HINT 1: Think about using the Python Slice Operator
# news_path = os.path.join(os.path.dirname(__file__), "news.json")
# with open(news_path, "r") as file:
#     news_data = json.load(file)
#     file.close()

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


## STEP 3: Use twilio.com/docs/sms/quickstart/python
# Send a separate message with each article's title and description to your phone number. 
#HINT 1: Consider using a List Comprehension.

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
calculate_difference()