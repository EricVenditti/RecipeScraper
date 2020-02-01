from bs4 import BeautifulSoup  # bs4 is beautiful soup
import requests
import json

def get_directions_for_link(url):

    response = requests.get(url, timeout=5)  # access url 5 times max
    content = BeautifulSoup(response.content, "html.parser")

    for direction in content.findAll('span', attrs={"class": "recipe-directions__list--item"}):
        print(direction.text)

    return direction.text

# TESTING
#get_directions_for_link('https://www.allrecipes.com/recipe/13721/fruit-salad/?internalSource=previously%20viewed&referringContentType=Homepage')