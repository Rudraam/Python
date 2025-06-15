#newapi.com

import requests
import json
import time
print("=====================================================================")
print("                Welcome to the Daily News                            ")
print("=====================================================================")
tim = time.strftime("%H :%M :%S")
name = input("Enter your name: ")
print(tim)
print(f"{name}, Welcome to our app!!")
query= input("What type of news are you interested in?")
url=f"https://newsapi.org/v2/everything?q={query}&from=2025-05-15&sortBy=publishedAt&apiKey=06d4b8022d644dd9a894915102882352"
r = requests.get(url)
news= json.loads(r.text)
# print(news)

for article in news["articles"]:
    print(article["title"])
    print(article["description"])
    print("------------------------------------------------------------------") 