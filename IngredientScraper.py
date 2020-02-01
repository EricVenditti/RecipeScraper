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

#url = 'https://www.allrecipes.com/recipe/14064/easy-guacamole/'
#print(url)



def get_ingredients(url):
    response = requests.get(url, timeout=5)  # access url 5 times max
    content = BeautifulSoup(response.content, "html.parser")
    ingredients = []

    nonIngredientList = ["teaspoon", "dessertspoon", "tablespoon", "ounce", "pound",
                        "cup", "pint", "quart", "gallon",
                        "can", "bag", "package", "bulk",
                        "pinch", "smidgen", "drop", "dash", "scruple", "coffeespoon", "pinches", "smidgens", "dashes", "clove",
                        "firmly packed", "lightly packed", "even", "level", "rounded", "sifted",
                        "chopped", "peeled", "seeded", "grated", "grilled", "layered", "melted", "scrambled","sliced", "spread", "blended",
                        "fresh", "stalk", "drained", "pitted", "peeled", "beaten",
                        "salt", "olive oil", "conola oil", "vegetable oil", "water", "hot water", "boiling water",
                        "to taste", "add to taste", "optional"]

    tempList = nonIngredientList.copy()
    for item in tempList:
        nonIngredientList.append(item + "s")
    nonIngredientList.reverse()

    for ingredient in content.findAll('span', attrs={"itemprop": "recipeIngredient"}):
        ingredientText = ingredient.text
        ingredientText = ''.join([i for i in ingredientText if (i.isalpha() or i == ' ')])
        # remove all the non-necessary adjectives, verbs, measurements in the ingredient list
        # preparing for searching grocery stores
        ingredientText = ingredientText.lstrip()  # gets rid of leading/trailing spaces
        andLoc = ingredientText.find(" and")
        # if there is an "and ..." string, return a string without it (seems to be very common with recipes
        if(andLoc != -1):
            ingredientText = ingredientText[: andLoc]
        for word in nonIngredientList:
            ingredientText = ingredientText.replace(word, "")   # removes words from the list
        ingredientText = ingredientText.lstrip()  # gets rid of leading/trailing spaces (L and R)
        ingredientText = ingredientText.rstrip()
        if(len(ingredientText) > 0):              # removes empty strings (i.e. "salt" would be removed and return "\n"
            ingredients.append(ingredientText)

    # json dump
    with open('ingredients.json', 'w') as outfile:
        json.dump(ingredients, outfile)

    # select all <p> paragraph tags with tag content .text(only text
    # contents of the file)
    with open('ingredients.json') as json_data:
        jsonData = json.load(json_data)

    return ingredients
