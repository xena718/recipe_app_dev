"""Server for recipes app."""

from flask import (Flask, render_template, request, flash, session, 
                    redirect)

from model import connect_to_db, db
import crud

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev" #It’ll need a secret key (otherwise, flash and session won’t work)
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """view homepage"""

    return render_template("homepage.html")


@app.route("/recipes/<recipe_id>")
def show_recipe(recipe_id):
    """Show details on a particular recipe."""

    recipe = crud.get_recipe_by_recipe_id(recipe_id)
    

    return render_template("recipe_details.html", recipe=recipe)

@app.route("/<shoppinglist_id>")
def show_shoppinglist(shoppinglist_id):
    """Show shoppinglist of the currently logged in user"""

    

    return render_template("recipe_details.html", recipe=recipe)


if __name__ == "__main__":
    connect_to_db(app) # connect to your database before app.run gets called, so that Flask can access your database.
    app.run(host="0.0.0.0", debug=True)
