from bs4 import BeautifulSoup  # bs4 is beautiful soup
import requests
import json

#url = 'https://www.allrecipes.com/recipe/13721/fruit-salad/?internalSource=previously%20viewed&referringContentType=Homepage'
#print(url)
def get_directions_for_link(url):

    response = requests.get(url, timeout=5)  # access url 5 times max
    content = BeautifulSoup(response.content, "html.parser")
    #directions = []

    for direction in content.findAll('span', attrs={"class": "recipe-directions__list--item"}):
        print(direction.text)

    #with open('directions.json', 'w') as outfile:
    #    json.dump(directions, outfile)

    #with open('directions.json') as json_data:
    #    jsonData = json.load(json_data)
    return direction.text

# TESTING
#get_directions_for_link('https://www.allrecipes.com/recipe/13721/fruit-salad/?internalSource=previously%20viewed&referringContentType=Homepage')