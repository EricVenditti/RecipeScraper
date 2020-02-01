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
item = "guac"#input("enter in what you would like to cook")
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
for recipe in content.findAll('span', attrs={"class": "stars stars-5"}):
    recipeObject = {
        "rating": recipe.attrs['data-ratingstars']
    }
    recipes.append(recipeObject)

# for tweetObject in tweetArr:
#	print(tweetObject)

with open('recipes.json', 'w') as outfile:
    json.dump(recipes, outfile)

# select all <p> paragraph tags with tag content .text(only text
# contents of the file)
with open('recipes.json') as json_data:
    jsonData = json.load(json_data)
for i in jsonData:
    print(i['rating'])
    #if (i['price'].find("$") == -1): continue