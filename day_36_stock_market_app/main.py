import datetime
import requests


STOCK = "KLTR"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
# get yesterday date
yesterday = str(datetime.date.today() - datetime.timedelta(days=1))
day_before_yesterday = str(datetime.date.today() - datetime.timedelta(days=2))

## STEP 1: Use https://newsapi.org/docs/endpoints/everything
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
#HINT 1: Get the closing price for yesterday and the day before yesterday. Find the positive difference between the two prices. e.g. 40 - 20 = -20, but the positive difference is 20.
#HINT 2: Work out the value of 5% of yerstday's closing stock price. 

parameters = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK,
    "apikey": "your api here",
}
news_parameters = {
    "function": "NEWS_SENTIMENT",
    "symbol": STOCK,
    "apikey": "your api here",

}

response = requests.get(STOCK_ENDPOINT, params=parameters)
data = response.json()

yesterday_closing_price = data["Time Series (Daily)"][yesterday]["1. open"]
day_before_yesterday_price = data["Time Series (Daily)"][day_before_yesterday]["4. close"]

# Calculate the diference between yesterday_closing_price and day_before_yesterday_price in %
def calculate_diference():
    percentage_difference = ((float(yesterday_closing_price) - float(day_before_yesterday_price)) / float(day_before_yesterday_price)) * 100
    print(percentage_difference )
    if percentage_difference > 2 or percentage_difference < -2:
        print("Get News")
        get_news()
    else:
        print("No News")

## STEP 2: Use https://newsapi.org/docs/endpoints/everything
# Instead of printing ("Get News"), actually fetch the first 3 articles for the COMPANY_NAME. 
#HINT 1: Think about using the Python Slice Operator
def get_news():
    news_response  = requests.get(STOCK_ENDPOINT,params=news_parameters)
    news_data = news_response.json()
    for i, news in enumerate(news_data["articles"][:3]):
        print(f"Headline: {news['title']}\nBrief: {news['description']}\n")
        print("---")
        print(f"Link: {news['url']}\n")
        print("---")
        if i == 2:
            break
   
    


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
calculate_diference()