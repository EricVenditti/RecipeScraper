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

url = 'https://www.allrecipes.com/recipe/13721/fruit-salad/?internalSource=previously%20viewed&referringContentType=Homepage'
print(url)

response = requests.get(url, timeout=5)  # access url 5 times max
content = BeautifulSoup(response.content, "html.parser")
directions = []

#print(content.prettify())
#step = content.find('div', attrs={"class": "toggle-similar__title"})
#link = content.find('a').get('href')
#print(step)
#print(link)
# step = content.find('div', attrs={"class": "direction-lists"}).text
# print(step)
# creating json objects with KEY: VALUE

for direction in content.findAll('span', attrs={"class": "recipe-directions__list--item"}):
    print(direction.text)

with open('directions.json', 'w') as outfile:
    json.dump(directions, outfile)

# select all <p> paragraph tags with tag content .text(only text
# contents of the file)
with open('directions.json') as json_data:
    jsonData = json.load(json_data)
