import requests
from send_email import send_email

api_key = "41d51d4165de42359b80cd075e55372c"
url = "https://newsapi.org/v2/top-headlines?sources=techcrunch&apiKey=41d51d4165de42359b80cd075e55372c"

request = requests.get(url)
content = request.json()
news = dict()
raw_message = ""

for article in content["articles"]:
    if article["title"] is not None:
        news[article["title"]] = article["description"] + "\n" + article["url"]

for key, value in news.items():
    raw_message += f"{key}" + "\n" + f"{value} \n \n"

message = f"""\
Subject: Today's news    
{raw_message}"""

send_email(message)




