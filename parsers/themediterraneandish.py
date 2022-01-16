import re

from bs4 import BeautifulSoup

# This parser only works for *some* recipes.
# Site has two different html schemes for recipes... 
def parse(html):
    soup = BeautifulSoup(html, "html5lib")
    
    # Get ingredients
    recipe = {
        'title': "",
        'yield': "N/A",
        'ingredients': [],
        'instructions': [],
    }
    
    recipe['title'] = soup.find(class_='wprm-recipe-name').get_text()

    recipe['yield'] = soup.find(class_='wprm-recipe-servings-with-unit').get_text()
    
    ingredientsRS = soup.find_all(class_='wprm-recipe-ingredient')
    for index, ingredientTag in enumerate(ingredientsRS):
        # Skip first entry which is always a "select all" for the site's checkbox
        if index == 0:
            continue
        # All ingredients are prefixed with empty checkbox character;
        # we want to ignore that
        recipe['ingredients'].append(ingredientTag.get_text()[1:])

    instructionsRS = soup.find_all(class_='wprm-recipe-instruction-text')
    for instructTag in instructionsRS:
        recipe['instructions'].append(instructTag.get_text())
    
    return recipe
