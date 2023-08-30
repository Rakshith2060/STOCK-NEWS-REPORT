import requests
from twilio.rest import Client
STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"
STOCK_API_KEY = "PW3SGL66D18REKRI"
NEWS_API_KEY = "1e22fa09d42540f8808e726d4ee27a73"
TWILIO_SID = "ACf6182316bff0c353731f9e92c8cfa"
TWILIO_AUTH_TOKEN = "45c845d41fc6bcdb324a6c708d11e7fb"
    ## STEP 1: Use https://www.alphavantage.co/documentation/#daily
# When stock price increase/decreases by 5% between yesterday and the day before yesterday then print("Get News").

#TODO 1. - Get yesterday's closing stock price. Hint: You can perform list comprehensions on Python dictionaries. e.g. [new_value for (key, value) in dictionary.items()]
STOCK_PARAMS = {
        "function" : "TIME_SERIES_DAILY",
        "symbol" : STOCK_NAME,
        "apikey": STOCK_API_KEY

}
response = requests.get(STOCK_ENDPOINT, params=STOCK_PARAMS)
data = response.json()["Time Series (Daily)"]
data_list = [value for (key,value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_data = yesterday_data["4. close"]
print(yesterday_closing_data)
#TODO 2. - Get the day before yesterday's closing stock price
day_before_yesterday_closing_data = data_list[1]["4. close"]
print(day_before_yesterday_closing_data)

#TODO 3. - Find the positive difference between 1 difference is 20. Hint: https://www.w3schools.com/python/ref_func_abs.aspand 2. e.g. 40 - 20 = -20, but the positive
difference = abs(float(yesterday_closing_data) - float(day_before_yesterday_closing_data))
print(difference)

#TODO 4. - Work out the percentage difference in price between closing price yesterday and closing price the day before yesterday.
percentage_difference = (difference / float(yesterday_closing_data)) * 100
print(percentage_difference)
#TODO 5. - If TODO4 percentage is greater than 5 then print("Get News").
NEWS_PARAMS = {
        "apiKey" : NEWS_API_KEY,
        "q" : COMPANY_NAME
}
if difference > 5:
        news_response = requests.get(NEWS_API_KEY, params=NEWS_PARAMS)
        articles = news_response.json()["articles"]
    ## STEP 2: https://newsapi.org/ 
    # Instead of printing ("Get News"), actually get the first 3 news pieces for the COMPANY_NAME. 

#TODO 6. - Instead of printing ("Get News"), use the News API to get articles related to the COMPANY_NAME.
        three_articles = articles[:3]
        print(three_articles)
#TODO 7. - Use Python slice operator to create a list that contains the first 3 articles. Hint: https://stackoverflow.com/questions/509211/understanding-slice-notation


    ## STEP 3: Use twilio.com/docs/sms/quickstart/python
    #to send a separate message with each article's title and description to your phone number. 

#TODO 8. - Create a new list of the first 3 article's headline and description using list comprehension.
        formatted_article = [f"Headline: {article['title']}. \nBrief: {article['description']}" for article in three_articles]
#TODO 9. - Send each article as a separate message via Twilio. 

        client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)


#Optional TODO: Format the message like this:
        for article in formatted_article:
                message = client.messages.create(
                        body = article,
                        from_ = "+15167386982",
                        to = "+919027362823"
                )
"""
TSLA: 🔺2%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
or
"TSLA: 🔻5%
Headline: Were Hedge Funds Right About Piling Into Tesla Inc. (TSLA)?. 
Brief: We at Insider Monkey have gone over 821 13F filings that hedge funds and prominent investors are required to file by the SEC The 13F filings show the funds' and investors' portfolio positions as of March 31st, near the height of the coronavirus market crash.
"""

