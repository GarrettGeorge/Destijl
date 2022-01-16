import re

from bs4 import BeautifulSoup

def parse(html):
    soup = BeautifulSoup(html, "html5lib")
    
    # Get ingredients
    
    title = soup.find(attrs={'data-testid': "ContentHeaderHed"}).get_text()

    # We can't drill down to the list immediately because the yield is
    # a sibling
    ingredientList = soup.find(attrs={'data-testid': "IngredientList"})
    recipe_yield = ingredientList.find(class_=re.compile('Yield-'))

    ingredientList = ingredientList.find(class_=re.compile('List-'))
    descriptions = ingredientList.find_all(class_=re.compile('Description-'))
    
    recipe = {
        'title': title,
        'yield': recipe_yield.get_text(),
        'ingredients': [],
        'instructions': [],
    }
    for descTag in descriptions:
        recipe['ingredients'].append(descTag.get_text())

    #  Get instructions
    instructions = soup.find(class_=re.compile('InstructionGroupWrapper-'))\
        .find_all(class_=re.compile('InstructionBody-'))
    for s in instructions:
        recipe['instructions'].append(s.get_text())

    return recipe
