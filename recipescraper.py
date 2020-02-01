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
item = input("enter in what you would like to cook")
url = 'https://www.allrecipes.com/search/results/?wt=' + str(item) + '&sort=re'
print(url)

response = requests.get(url, timeout=5)  # access url 5 times max
content = BeautifulSoup(response.content, "html.parser")
recipes = []
#print(content.prettify())
#step = content.find('div', attrs={"class": "toggle-similar__title"})
#link = content.find('a').get('href')
#print(step)
#print(link)
# step = content.find('div', attrs={"class": "direction-lists"}).text
# print(step)
# creating json objects with KEY: VALUE
link = content.find('a').get('href')
print(link)
for recipe in content.findAll('article', attrs={"class": "fixed-recipe-card"}):
    print("hi")
    recipeObject = {
        "link": recipe.find('a', attrs={"href"}),
        #gu"2tag": recipe.find('span', attrs={"itemprop": "name"}).text,
        #"date": recipe.find('h5', attrs={"class": "dateTime"}).text,
        #"tweet": recipe.find('p', attrs={"class": "content"}).text
        # "likes": tweet.find('p', attrs={"class": "likes"}),
        # "shares": tweet.find('p', attrs={"class": "shares"})
    }
    recipes.append(recipeObject)

# for tweetObject in tweetArr:
#	print(tweetObject)

with open('recipes.json', 'w') as outfile:
    json.dump(recipes, outfile)

# select all <p> paragraph tags with tag content .text(only text
# contents of the file)
