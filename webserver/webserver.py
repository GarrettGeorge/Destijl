from flask import Flask, render_template
app = Flask(__name__, template_folder='templates')

import core.core as core

@app.route('/')
def hello_world():
   return 'Hello World'

@app.route('/<path:path>')
def handleRecipeUrl(path):
    try:
        recipeJson = core.getJson(path)
        metadata = {
            'recipeUrl': path,
        }
        return render_template('recipe.html', metadata=metadata, recipe=recipeJson)
    except Exception as err:
        print(err)
        return render_template('error.html')

def run():
    app.run(port=8123)