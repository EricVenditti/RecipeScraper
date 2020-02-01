from bs4 import BeautifulSoup  # bs4 is beautiful soup
import requests
import json

'''
python requests libary has 3 parts 
URL: The link of the website we are accessing  

RESPONSE: result of a GET request. actually an HTTP status code.
success is 200. troubleshoot codes at restapitutorial.com

CONTENT: the content we'd like to grab/print
'''
url = 'https://www.allrecipes.com/recipes/105/appetizers-and-snacks/dips-and-spreads/?internalSource=recipe%20breadcrumb&referringId=14231&referringContentType=Recipe&referringPosition=1&clickId=recipe%20breadcrumb%204/'
response = requests.get(url, timeout=5)  # access url 5 times max
content = BeautifulSoup(response.content, "html.parser")
recipes = []
print(content)
# step = content.find('div', attrs={"class": "direction-lists"}).text
# print(step)
# creating json objects with KEY: VALUE
'''
for tweet in content.findAll('div', attrs={"class": "tweetcontainer"}):
    tweetObject = {
        "author": tweet.find('h2', attrs={"class": "author"}).text,
        "date": tweet.find('h5', attrs={"class": "dateTime"}).text,
        "tweet": tweet.find('p', attrs={"class": "content"}).text
        # "likes": tweet.find('p', attrs={"class": "likes"}),
        # "shares": tweet.find('p', attrs={"class": "shares"})
    }
    tweetArr.append(tweetObject)

# for tweetObject in tweetArr:
#	print(tweetObject)

with open('twitterData.json', 'w') as outfile:
    json.dump(tweetArr, outfile)

# select all <p> paragraph tags with tag content .text(only text
# contents of the file)
'''
