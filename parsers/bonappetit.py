import re

from bs4 import BeautifulSoup

def parse(html):
    soup = BeautifulSoup(html, "html5lib")
    
    # Get ingredients
    
    # We can't drill down to the list immediately because the yield is
    # a sibling
    ingredientList = soup.find(attrs={'data-testid': "IngredientList"})
    recipe_yield = ingredientList.find(class_=re.compile('Yield-'))

    ingredientList = ingredientList.find(class_=re.compile('List-'))
    amounts = ingredientList.find_all(class_=re.compile('Amount-'))
    descriptions = ingredientList.find_all(class_=re.compile('Description-'))
    
    recipe = {
        'yield': recipe_yield.get_text(),
        'ingredients': {},
        'steps': [],
    }
    for i in range(len(amounts)):
        recipe["ingredients"][descriptions[i].get_text()] = amounts[i].get_text()

    #  Get steps
    steps = soup.find(class_=re.compile('InstructionGroupWrapper-'))\
        .find_all(class_=re.compile('InstructionBody-'))
    for s in steps:
        recipe['steps'].append(s.get_text())

    return recipe
