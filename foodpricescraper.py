from bs4 import BeautifulSoup  # bs4 is beautiful soup
import requests
import json

item = "pie"

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

# just a simple output
for i in jsonData:
    if (i['price'].find("$") == -1): continue
    print(i['price'])