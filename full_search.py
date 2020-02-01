from recipescraper		import *
from foodpricescraper	import *
from IngredientScraper	import *
from DirectionScraper	import *

def get_top_five(recipe_name):
    temp_arr = get_recipes_for_search(recipe_name)
    ret_arr = []
    
    for i in range(5):
        ret_arr.append({"Picture": temp_arr[i]["img"], "Description": temp_arr[i]["desc"]})
    print(ret_arr)
    return ret_arr

def get_stuff(recipe_name):
	temp_arr = get_recipes_for_search(recipe_name)
	if (len(temp_arr) == 0): 
		print("no recipes found for keyword")
		return
	url = temp_arr[0]["link"]
	print(get_directions_for_link(url))
	ing = get_ingredients(url)
	print("Ingredients:")
	for i in ing:
		print("\t" + i)
	#print(ing)
	print("$" + str(get_price_for_list(get_ingredients(url))))


#get_stuff("guac")