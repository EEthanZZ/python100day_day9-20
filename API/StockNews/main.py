import requests
from datetime import date, timedelta
from twilio.rest import Client

yesterday = str(date.today() - timedelta(days=1))
day_before_yesterday = str(date.today() - timedelta(days=2))
print(yesterday)
print(day_before_yesterday)
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

TWI_SID = "AC185eb2acbcdee217a8e18b6a364a56bf"
TWI_TOKEN = "efeebd9f13ed8e0f593e2158261f40fa"
TWI_NUM = "+16614864166"

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

# TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
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
    response_new = requests.get(url=NEWS_ENDPOINT, params=news_para)
    news = response_new.json()
    print(f"{COMPANY_NAME}: {difference_in_percentage}")
    for i in range(0, 3):
        news_titles = news["articles"][i]["title"]
        news_brief = news["articles"][i]["description"]
        print(f"Headline: {news_titles}")
        print(f"Brief: {news_brief}")

        account_sid = TWI_SID
        auth_token = TWI_TOKEN
        client = Client(account_sid, auth_token)

        message = client.messages \
            .create(
            body=f"Headline: {news_titles}\nBrief: {news_brief}",
            from_=TWI_NUM,
            to='+61404346835'
        )

        print(message.sid)

# TODO 9. - Send each article as a separate message via Twilio.


# Optional TODO: Format the message like this:
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""
