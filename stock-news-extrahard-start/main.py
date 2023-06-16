from twilio.rest import Client
STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"
import requests
import datetime

## STEP 1: Use https://www.alphavantage.co
# When STOCK price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").
today = datetime.date.today()

yesterday = today - datetime.timedelta(days=1)
the_day_before_yesterday = today - datetime.timedelta(days=2)

STOCK_API_KEY = "44ZKLFGM4ONV6ZH5"
API_ALPHAVANTAGE = "https://www.alphavantage.co/query"

stock_parameters = {
    "function" : "TIME_SERIES_DAILY_ADJUSTED",
    "symbol": STOCK,
    "interval": "5min",
    "apikey": STOCK_API_KEY
}

NEWS_API_KEY = "ec914476472149ddaa0bc04aaf7b2c0f"
API_NEWS = "https://newsapi.org/v2/everything"

news_parameters = {
    "q": COMPANY_NAME,
    "from": yesterday,
    "sortBy": "popularity",
    "apiKey": NEWS_API_KEY
}

account_sid = "AC3a99640e24bc06a3a7c0f2d556aabb74"
auth_token = "63158653b4d5100b098f4fb8cc2c97d5"

response_stock = requests.get(url=API_ALPHAVANTAGE, params=stock_parameters)
response_stock.raise_for_status()
stock_data = response_stock.json()
stock_daily = stock_data["Time Series (Daily)"]

yesterday_close = stock_daily[f"{yesterday}"]["4. close"]
the_day_before_yesterday_close = stock_daily[f"{the_day_before_yesterday}"]["4. close"]

difference = round((float(yesterday_close) - float(the_day_before_yesterday_close))/float(yesterday_close) * 100)
if difference > 0:
    sign = "🔺"
else:
    sign = "🔻"
## STEP 2: Use https://newsapi.org
# Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME.
if abs(difference) >= 5:
    response_news = requests.get(url=API_NEWS, params=news_parameters)
    response_news.raise_for_status()
    news_data = response_news.json()
    for article in news_data["articles"][:3]:
        title = article["title"]
        description = article["description"]
        client = Client(account_sid, auth_token)
        message = client.messages.create(
            body=f"{STOCK} {sign} {difference}%\n Headline: {title}\n Brief: {description}",
            from_='+12706757625',
            to='+48697020791'
        )
        print(message.status)


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

