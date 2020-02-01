from bs4 import BeautifulSoup  # bs4 is beautiful soup
import requests
import json
import statistics

from util import * # see util.py

#item = "banana"

def metro_food_search(item):
    print_arr = False
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
    count = 0
    for food_item in content.findAll('div', attrs={"class":"pt-title"}):
        if (count >= len(price_arr)): break
        price_arr[count]["name"] = food_item.contents[0]
        count += 1
        #print(food_item.contents)
    
    # remove items with names more than 3x longer than search word
    # so that stuff like "salted banana crisps" don't appear when you search for "banana"
    num_spaces_search = item.count(" ") + 1
    price_arr_bkup = price_arr.copy()
    for food in price_arr:
        word_count = food["name"].count(" ") + 1 
        if (word_count > (num_spaces_search * 3)):
            price_arr.remove(food)
    if (len(price_arr) == 0): price_arr = price_arr_bkup # restore if it removes all items

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

def get_price(item):
    if (item == None or item == ""): return 0.0
    price_arr = metro_food_search(item)
    if (len(price_arr) == 0): return 0.0
    price = statistics.mean(metro_food_search(item))
    #print (price)
    return price

def get_price_for_list(list):
    total = 0
    for item in list:
        total += get_price(item)
    return total

items = ["avocados", "tomatoes", "onion", "cilantro", "lemon juice", "jalapeno pepper"]
# TESTING

#for item in items:
#    print(item)
#    metro_food_search(item)

#with open('recipes.json','r') as f:
#    recipes_dict = json.load(f)
#    print(json.dumps(recipes_dict, indent = 4, sort_keys=True)) # prettified printing
#for r in recipes_dict:
#    print(r["desc"])
#    metro_food_search(r["desc"]) # should be changed to ingredients instead
print("banana")
print(get_price("banana"))
print("items")
print(get_price_for_list(items))

#print("banana")
#metro_food_search("banana")
#print("apple")
#metro_food_search("apple")
#print("pie")
#metro_food_search("pie")
print("shit pie")               # test for something metro doesn't have
metro_food_search("shit pie")
get_price("shit pie")