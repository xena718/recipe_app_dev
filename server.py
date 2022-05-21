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

@app.route('/logout')
def logout():
    #user has logged in already before user can access logout route
    del session["logged_in_user_email"]
    flash ("logged out")
    return redirect('/')

@app.route('/account')
def show_account():

    user_email = session["logged_in_user_email"]
    if not user_email:
        flash("please log in first to access account")
        return redirect('/signup-login') 

    user = crud.get_user_by_email(user_email)
    user_added_recipes = user.added_recipes 
    #use the added_recipes attribute to access user added recipes
    #user_added_recipes and user_added_recipes are both list.
    user_saved_recipes = user.saved_recipes

    return render_template("user_account.html", logged_in_user=user, user_saved_recipes=user_saved_recipes, user_added_recipes=user_added_recipes)




@app.route("/add-to-saved/<recipe_id>", methods=["POST"])
def add_to_saved(recipe_id):
    user_email = session["logged_in_user_email"]
    if not user_email:
        flash("please log in first to save a recipe")
        return redirect('/signup-login')
    
    # print("*"*20+user_email)
    user = crud.get_user_by_email(user_email)
    recipe = crud.get_recipe_by_recipe_id(recipe_id)
    
    # check if recipe_id in saved_recipes table already. 
    # user.saved_recipes: a list of Saved_Recipe object
    # can do list comprehension
    saved_recipe_ids = [saved_recipe.recipe_id for saved_recipe in user.saved_recipes]
    
    if recipe.recipe_id in saved_recipe_ids:
        flash("Added already")
        return redirect('/')

    else:
        #create a saved_recipe object 
        saved_recipe = crud.create_saved_recipe(user.user_id, recipe.recipe_id)
        # user.saved_recipes.append(recipe) #assication between user and saved recipes
        db.session.add(saved_recipe)
        db.session.commit() 

        flash(f"aded recipe #{recipe.recipe_id} to your saved recipe collections")
        return redirect('/')

@app.route("/remove-from-saved/<recipe_id>", methods=["POST"])
def remove_recipe_from_saved(recipe_id):
    #user must have logged in before user is routed to this route.
    user_email = session["logged_in_user_email"]
    user = crud.get_user_by_email(user_email)
    recipe = crud.get_recipe_by_recipe_id(recipe_id)
    saved_recipe_entry = crud.get_saved_recipe_by_recipe_id(recipe_id)
    
    #delete the saved_recipe_entry 
    db.session.delete(saved_recipe_entry)
    db.session.commit()

    return redirect('/saved')



@app.route("/saved")
def show_saved_recipes_by_user():
    user_email = session["logged_in_user_email"]
    if not user_email:
        flash("please log in first to access saved recipe collections")
        return redirect('/signup-login')
    
    user = crud.get_user_by_email(user_email)
    
    # user.saved_recipes: a list of recipe object that were saved by user.
    user_saved_recipes = user.saved_recipes

    return render_template("saved_recipes.html", saved_recipes=user_saved_recipes)   




@app.route("/recipe/<recipe_id>")
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
