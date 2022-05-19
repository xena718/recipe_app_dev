"""Server for recipes app."""

from flask import (Flask, render_template, request, flash, session, 
                    redirect)

from model import connect_to_db, db
import crud
import random

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev" #It’ll need a secret key (otherwise, flash and session won’t work)
app.jinja_env.undefined = StrictUndefined


@app.route('/')
def homepage():
    """view homepage"""

    # all_recipes = crud.get_all_recipes()
    cuisines = ["American", "British", "Caribbean", "Chinese", "French", "Greek", "Indian", "Italian", "Japanese", "Mediterranean", "Mexican", "Moroccan", "Spanish", "Thai", "Turkish", "Vietnamese", "Food Fusion", "Others"]
    
    one_recipe_per_cuisine = []
    for cuisine_name in cuisines:
        cuisine_instance = crud.get_cuisine_by_name(cuisine_name)
        recipes_by_cuisine_id = crud.get_recipes_by_cuisine_id(cuisine_instance.cuisine_id)
        one_recipe_per_cuisine_id = random.choice(recipes_by_cuisine_id)
        one_recipe_per_cuisine.append(one_recipe_per_cuisine_id)    

    return render_template("homepage.html", recipes_cuisines=one_recipe_per_cuisine)

@app.route('/signup-login')
def show_signup_login_page():
    """show the page for signup_login"""
    return render_template("signup_login.html")
    

@app.route('/login', methods=['POST'])
def process_login():
    """parse user login information
    Find the user's login credentials located in the 'request.form'
    dictionary, look up the user, and store them in the session.
    """
    email = request.form.get("email")
    password = request.form.get("password")
    
    user = crud.get_user_by_email(email)

    if not user:
        flash("No user exists with entered email")
        return redirect('/signup-login')
    if password != user.password:
        flash("Invalid password")
        return redirect('/signup-login')
    
    session["logged_in_user_email"] = email #store user email in session. Can you store user instance

    flash(f"Hello, {user.name}!")
    return redirect('/')


@app.route('/signup', methods=['POST'])
def register_user():
    """parse user sign up information, create a new user if it doesn't exist,
    and store user information in the database"""

    email = request.form.get('email')
    name =request.form.get('name')
    password = request.form.get('password')

    user_by_email = crud.get_user_by_email(email)
    user_by_name = crud.get_user_by_name(name)
    
    if user_by_email:
        flash("This email address has been registered. Try a different email address.")
    if user_by_name:
        flash("This name has been registered. Please try a different one")

    new_user = crud.create_user(email, name, password)
    db.session.add(new_user)
    db.session.commit()
    flash("Account successfully created. Please log in")

    return redirect('/signup-login')


@app.route("/add-to-saved", methods=["POST"])
def add_to_saved():
    user_email = session["logged_in_user_email"]
    if not user_email:
        flash("please log in first to access saved recipe collections")
        # return redirect('/signup-login')
    user = crud.get_user_by_email(user_email)
    recipe_to_be_saved = request.form.get('submit')
    user.saved_recipes.append(db_recipe) #assication between user and saved recipes
    db.session.commit() # can i just commit in this way?
    return redirect('/signup-login')

@app.route("/<user_id>/saved")
def show_saved_recipes_by_user(user_id):
    user_email = session["logged_in_user_email"]
    if not user_email:
        flash("please log in first to access saved recipe collections")
        return redirect('/signup-login')
    
    user = crud.get_user_by_email(user_email)
    user_saved_recipes = user.saved_recipes

    return render_template("saved_recipes.html", saved_recipes=user_saved_recipes)   




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
