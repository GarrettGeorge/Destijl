import re
import json

from bs4 import BeautifulSoup

def parse(html):
    soup = BeautifulSoup(html, "html5lib")
    
    ingredientList = soup.find('script').contents[0]
    pageJson = json.loads(ingredientList)

    recipe = {
        'yield': '',
        'ingredients': [],
        'instructions': [],
    }

    for item in pageJson:
        if "recipeIngredient" in item:
            recipe['ingredients'].append(item['recipeIngredient'])  

    return recipe