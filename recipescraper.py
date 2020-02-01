from bs4 import BeautifulSoup  # bs4 is beautiful soup
import requests
import json
import re


def get_recipes_for_search(item):
    #item = "guac"#input("enter in what you would like to cook: ")
    url = 'https://www.allrecipes.com/search/results/?wt=' + str(item) + '&sort=re'
    #print(url)

    response = requests.get(url, timeout=5)  # access url 5 times max
    content = BeautifulSoup(response.content, "html.parser")
    recipes = []

    # ratings
    for recipe in content.findAll('span', attrs={'class': re.compile("^stars stars-.*")}):  #stars stars-5 is the 5 stars image heading. This looks for all ratings
        recipes.append({"rating": recipe.attrs["data-ratingstars"]})

    # number of ratings
    count = 0
    for num in content.findAll("span", attrs={'class': "fixed-recipe-card__reviews"}):
        recipes[count]["num_reviews"] = num.contents[0].attrs['number']
        count += 1

    # picture + description
    count = 0
    for num in content.findAll("img", attrs={'class': "fixed-recipe-card__img"}):
        recipes[count]["img"] = num.attrs['data-original-src']
        recipes[count]["desc"] = num.attrs['alt']
        count += 1

    # link
    count = 0
    for recipe in content.findAll('h3', attrs = {"class": "fixed-recipe-card__h3"}):
        recipes[count]["link"] = recipe.contents[1].attrs['href']
        count += 1


    with open('recipes.json', 'w') as outfile:
        json.dump(recipes, outfile)

    with open('recipes.json') as json_data:
        jsonData = json.load(json_data)
    return jsonData

# TESTING CODE
#print("guac")
#get_recipes_for_search("guac")
#print("mexican")
#get_recipes_for_search("mexican")
#print("dutch oven apple crisp")
#get_recipes_for_search("dutch oven apple crisp")