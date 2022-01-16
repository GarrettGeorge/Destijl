import re

from bs4 import BeautifulSoup

def parse(html):
    soup = BeautifulSoup(html, "html5lib")
    
    # Get ingredients
    recipe = {
        'title': "",
        'yield': "N/A",
        'ingredients': [],
        'instructions': [],
    }
    
    recipe['title'] = soup.find(class_='assetTitle').get_text()

    recipe['yield'] = soup.find(class_='o-RecipeInfo__m-Yield')\
        .find(class_='o-RecipeInfo__a-Description').get_text()
    
    ingredientsRS = soup.find_all(class_=re.compile('Ingredient--CheckboxLabel'))
    for index, ingredientTag in enumerate(ingredientsRS):
        # Skip first entry which is always a "select all" for the site's checkbox
        if index == 0:
            continue
        recipe['ingredients'].append(ingredientTag.get_text().strip(" "))

    instructionsRS = soup.find_all(class_='o-Method__m-Step')
    for instructTag in instructionsRS:
        recipe['instructions'].append(instructTag.get_text().strip(" "))
    
    return recipe
