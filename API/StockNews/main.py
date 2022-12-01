import requests
from datetime import date, timedelta

yesterday = str(date.today() - timedelta(days=1))
day_before_yesterday = str(date.today() - timedelta(days=2))
print(yesterday)
print(day_before_yesterday)
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
STOCK_API = "Y2ZO48BKD979DZNA"
stock_para = {
    "function": "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK_NAME,
    "apikey": STOCK_API
}

NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
NEWS_API = "1732c7396c084730ae406cdff96427d1"
news_para = {
    "q": "tesla",
    "from": f"{yesterday}",
    "apiKey": NEWS_API,
}




    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
response = requests.get(url=STOCK_ENDPOINT, params=stock_para)
data = response.json()
stock_prices = data["Time Series (Daily)"]
stock_yesterday = stock_prices[yesterday]
stock_yesterday_close = float(stock_yesterday['4. close'])
print(stock_yesterday_close)

stock_before_yesterday_close = float(stock_prices[day_before_yesterday]['4. close'])
print(stock_before_yesterday_close)

difference = abs(stock_yesterday_close - stock_before_yesterday_close)
print(difference)

difference_in_percentage = difference / stock_before_yesterday_close
print(difference_in_percentage)

if difference_in_percentage == 0:
    print("get news")
    ## STEP 2: https://newsapi.org/
    response_new = requests.get(url=NEWS_ENDPOINT, params=news_para)
    news = response_new.json()
    print(news["articles"][0:2])

#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.

#TODO 9. - Send each article as a separate message via Twilio. 



#Optional TODO: Format the message like this: 
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

