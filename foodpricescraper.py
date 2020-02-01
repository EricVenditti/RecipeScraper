from bs4 import BeautifulSoup  # bs4 is beautiful soup
import requests
import json

from util import * # see util.py

#item = "banana"

def metro_food_search(item):
    print_arr = True
    url = 'https://www.metro.ca/en/search?filter=' + item + '&freeText=true'
    response = requests.get(url, timeout=5)  # access url 5 times max
    content = BeautifulSoup(response.content, "html.parser")
    price_arr = []
    for food_item in content.findAll('div', attrs={"class": "pi-sale-price"}):
        try:
            food_object = {
                "price": food_item.find("span", attrs={"class","pi-price price-update", "pi-price price-update pi-price-promo"}).text
            }
            price_arr.append(food_object)
        except:
            continue    # some weird pricing thing that I didn't account for

    with open('priceData.json', 'w') as outfile:
        json.dump(price_arr, outfile)

    with open('priceData.json') as json_data:
        jsonData = json.load(json_data)

    price_return_arr = []
    # just a simple output
    for i in jsonData:
        if (i['price'].find("$") == -1): continue
        price_return_arr.append(float(i['price'][1:])) # remove first character ("$", which was verified in the previous line), then convert to float
    
    price_return_arr = remove_outliers(price_return_arr)
    if (print_arr):                     # print if applicable
        for d in price_return_arr:
            print(str(d))
    
    return price_return_arr

items = ["avocados", "tomatoes", "onion", "cilantro", "lemon juice", "jalapeno pepper"]
# TESTING

for item in items:
    print(item)
    metro_food_search(item)

with open('recipes.json','r') as f:
    recipes_dict = json.load(f)
    print(json.dumps(recipes_dict, indent = 4, sort_keys=True)) # prettified printing
for r in recipes_dict:
    print(r["desc"])
    metro_food_search(r["desc"]) # should be changed to ingredients instead


print("banana")
metro_food_search("banana")
print("apple")
metro_food_search("apple")
print("pie")
metro_food_search("pie")
print("shit pie")               # test for something metro doesn't have
metro_food_search("shit pie")