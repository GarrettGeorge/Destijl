import re
import json

from bs4 import BeautifulSoup

def parse(html):
    soup = BeautifulSoup(html, "html5lib")
    
    ingredientList = soup.find('script').contents[0]
    pageJson = json.loads(ingredientList)
    recipe = {
        'title': '',
        'yield': '',
        'ingredients': [],
        'instructions': [],
    }

    for item in pageJson:
        if item['@type'] == "Recipe":
            recipe['title'] = item['name']
            recipe['yield'] = item['recipeYield']
            recipe['ingredients'] = item['recipeIngredient']
            recipe['instructions'] = list(map(lambda i: i['text'], item['recipeInstructions']))

    return recipe