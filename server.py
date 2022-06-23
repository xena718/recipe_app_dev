"""Server for recipes app."""

from flask import (Flask, render_template, request, flash, session, 
                    redirect)

from model import connect_to_db, db
import model # for query purpose

import crud
import random
from fractions import Fraction

from jinja2 import StrictUndefined

app = Flask(__name__)
app.secret_key = "dev" #It’ll need a secret key (otherwise, flash and session won’t work)
app.jinja_env.undefined = StrictUndefined

# #homepage before 0620version
# @app.route('/')
# def homepage():
#     """view homepage. Return one random recipe per cuisine"""
#     #one thing is improve is that heart of the recipe on homepage should be unfilled or filled if user logged in and the recipe has been saved by user

#     user_email = session.get("logged_in_user_email")
    
#     one_recipe_per_cuisine = []

#     # cuisines = ["American", "British", "Caribbean", "Chinese", "French", "Greek", "Indian", "Italian", "Japanese", "Mediterranean", "Mexican", "Moroccan", "Spanish", "Thai", "Turkish", "Vietnamese", "Food Fusion", "Others"]

#     ####### this following chunck works ###########
#     # for cuisine_name in cuisines:
#     #     cuisine_instance = crud.get_cuisine_by_name(cuisine_name)
#     #     recipes_by_cuisine_id = crud.get_recipes_by_cuisine_id(cuisine_instance.cuisine_id)
#     #     print("********************"+f"{cuisine_name} has the following recipes{recipes_by_cuisine_id}")
#     #     one_recipe_per_cuisine_id = random.choice(recipes_by_cuisine_id)
#     #     one_recipe_per_cuisine.append(one_recipe_per_cuisine_id)    
    
#     ########this following chunck doesn't work################
#     # crud.recipes_dbjoinedload_cuisine() 
#     # for cuisine_name in cuisines:
#     #     recipes_by_cuisine_name = crud.get_recipe_by_cuisine_name(cuisine_name)
#     #     print("********************"+f"{cuisine_name} has the following recipes{recipes_by_cuisine_name}")
#     #     one_recipe_each_cuisine = random.choice(recipes_by_cuisine_name)
#     #     one_recipe_per_cuisine.append(one_recipe_each_cuisine)    
#    ###################################################################
#     recipes = crud.recipes_dbjoinedload_cuisines() 
#     # print("********************"+f"{recipes[1]}, {recipes[1].cuisine.name}")
#     recipe_cuisine_names =[]

#     for recipe in recipes:
#         recipe_cuisine_name = recipe.cuisine.name
#         if recipe_cuisine_name in recipe_cuisine_names:
#             continue
#         else:
#             recipe_cuisine_names.append(recipe_cuisine_name)
#             one_recipe_per_cuisine.append(recipe)
#     if user_email:
#         current_user = crud.get_user_by_email(user_email)

#         return render_template("homepage.html", current_user=current_user, recipes_cuisines=one_recipe_per_cuisine)
#     else:
#         return render_template("homepage.html", recipes_cuisines=one_recipe_per_cuisine)


######homepage 0620version#########
@app.route('/')
def homepage():
    """
    view homepage. Return most saved recipe per cuisine.
    Allow user to browse by category.
    """
    user_email = session.get("logged_in_user_email")
    most_saved_recipe_per_cuisine = [] #if none of the recipes of the cuisine was saved, then no recipe for this cuisine
    
    ls_of_tp_recipe_id_count = crud.groupby_recipeid_orderby_count_for_saved_recipes()
    cuisines = ["American", "British", "Caribbean", "Chinese", "French", "Greek", "Indian", "Italian", "Japanese", "Mediterranean", "Mexican", "Moroccan", "Spanish", "Thai", "Turkish", "Vietnamese", "Food Fusion", "Others"]
    cuisines_copy = cuisines[:]

    for item in ls_of_tp_recipe_id_count:
        recipe_id, count = item
        recipe = crud.get_recipe_by_recipe_id(recipe_id)
        recipe_cuisine_name = recipe.cuisine.name
        if recipe_cuisine_name in cuisines_copy:
            cuisines_copy.remove(recipe_cuisine_name)
            most_saved_recipe_per_cuisine.append(recipe)
        else:
            continue
    # print("*"*20)
    # print(len(most_saved_recipe_per_cuisine))
    
    allrecipes_allcuisines = crud.get_allrecipes_allcuisines()
    allrecipes_allspecialdiets = crud.get_allrecipes_allspecialdiets()
    allrecipes_allcourses = crud.get_allrecipes_allcourses()

    if user_email:
        current_user = crud.get_user_by_email(user_email)
        return render_template("homepage.html", current_user=current_user, recipes_cuisines=most_saved_recipe_per_cuisine, allrecipes_allcuisines= allrecipes_allcuisines, allrecipes_allspecialdiets=allrecipes_allspecialdiets, allrecipes_allcourses=allrecipes_allcourses)
    else:
        return render_template("homepage.html", recipes_cuisines=most_saved_recipe_per_cuisine, allrecipes_allcuisines= allrecipes_allcuisines, allrecipes_allspecialdiets=allrecipes_allspecialdiets,allrecipes_allcourses=allrecipes_allcourses)

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

    user_email = session.get("logged_in_user_email")
    if not user_email:
        flash("please log in first to access account")
        return redirect('/signup-login') 

    user = crud.get_user_by_email(user_email)
    user_added_recipes = user.added_recipes 
    #use the added_recipes attribute to access user added recipes
    #user_added_recipes and user_added_recipes are both list.
    user_saved_recipes = user.saved_recipes

    return render_template("user_account.html", logged_in_user=user, user_saved_recipes=user_saved_recipes, user_added_recipes=user_added_recipes)

@app.route("/save-remove", methods=["POST"])
def save_remove():
    user_email = session.get("logged_in_user_email")
    if not user_email:
        flash("please log in first to save a recipe")
        return redirect('/signup-login')
    
    user = crud.get_user_by_email(user_email)
    recipe_id = request.json.get("recipeId")
    # print("*"*20+recipe_title)

    recipe = crud.get_recipe_by_recipe_id(recipe_id)
    saved_recipes_ids = [saved_recipe.recipe_id for saved_recipe in user.saved_recipes]
    
    if recipe.recipe_id in saved_recipes_ids:
        saved_recipe_entry = crud.get_saved_recipe_by_recipe_id(recipe_id)
        db.session.delete(saved_recipe_entry)
        db.session.commit()
        return "removed_from_saved"

    else:
        #create a saved_recipe object 
        saved_recipe = crud.create_saved_recipe(user.user_id, recipe.recipe_id)
        # saved_recipe = crud.create_saved_recipe(user, recipe)
        # user.saved_recipes.append(recipe) #assication between user and saved recipes
        db.session.add(saved_recipe)
        db.session.commit() 

        return "just_saved"

@app.route("/remove", methods=["POST"])
def remove_from_saved_recipes():
    #user must have logged in before user is routed to this route.
    # user_email = session["logged_in_user_email"]
    # user = crud.get_user_by_email(user_email)

    recipe_id = request.json.get("recipeId")
    recipe = crud.get_recipe_by_recipe_id(recipe_id)
    saved_recipe_entry = crud.get_saved_recipe_by_recipe_id(recipe_id)
    
    #delete the saved_recipe_entry 
    db.session.delete(saved_recipe_entry)
    db.session.commit()

    return "removed_from_saved" 


# <div class="card-btn-div">
#     <form action="/add-to-saved/{{ recipe.recipe_id }}" method="POST">
#     <button id="save-remove-btn" type="submit"><i class="bi bi-heart"></i></button>
#     </form>
# </div> 

@app.route("/add-to-saved/<recipe_id>", methods=["POST"])
def add_to_saved(recipe_id):
    user_email = session.get("logged_in_user_email")
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
        # saved_recipe = crud.create_saved_recipe(user, recipe)
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
    user_email = session.get("logged_in_user_email")
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
    user_email = session.get("logged_in_user_email")
    if user_email:
        current_user = crud.get_user_by_email(user_email)
        return render_template("recipe_details.html", current_user=current_user, recipe=recipe)

    else:    
        return render_template("recipe_details.html", recipe=recipe)

@app.route("/add-to-shoppinglist/<recipe_id>", methods=["POST"])
def add_ingredients_to_shoppinglist(recipe_id):
    """
    add static recipe ingredients from database to shopping list
    if servings size change, this route cannot handle it, but javascript AJAX can?.
    """
    user_email = session.get("logged_in_user_email")
    if not user_email:
        flash("please log in first to access saved recipe collections")
        return redirect('/signup-login')
    else:
        user = crud.get_user_by_email(user_email)
        shopping_recipe = crud.create_shopping_recipe(user.user_id, recipe_id)
        db.session.add(shopping_recipe)
        db.session.commit()

        flash("All ingredients addeded to your shoppinglist") 
        #noted that the actual action is to add recipe into shopping_recipe table.
        
        return redirect(f"/recipe/{recipe_id}")


@app.route("/shoppinglist")
def show_shoppinglist():
    """Show shoppinglist of the currently logged in user"""
    #TO BE UPDATED
    user_email = session.get("logged_in_user_email")
    if not user_email:
        flash("please log in first to access shopping list")
        return redirect('/signup-login')
    else:
        user = crud.get_user_by_email(user_email)
        # user.shopping_recipes: a list of recipe object that are added to shopping_list by user.
        shopping_recipes = user.shopping_recipes

        ###deal with ingredients (quantity and category)###
        ### update0522: will need to add unit###
        recipes_ingredients = crud.recipes_dbjoinedload_recipe_ingredients()
        ingredients_for_all_shopping_recipes ={}
        #{"catogery name": {ingredient_name:ingredient_quantity}
        
        for recipe in shopping_recipes:
            for ingredient in recipe.recipe_ingredients:
                if ingredient.category in ingredients_for_all_shopping_recipes:
                    if ingredient.quantity!="" and ingredient.quantity !=" ":
                        ingredients_for_all_shopping_recipes[ingredient.category][ingredient.name] = ingredients_for_all_shopping_recipes[ingredient.category].get(ingredient.name,0)+float(Fraction(ingredient.quantity))
                    else:
                        ingredients_for_all_shopping_recipes[ingredient.category][ingredient.name] = ingredients_for_all_shopping_recipes[ingredient.category].get(ingredient.name,0)
                        
                else:
                    ingredients_for_all_shopping_recipes[ingredient.category]={}
                    if ingredient.quantity!="" and ingredient.quantity !=" ":
                        ingredients_for_all_shopping_recipes[ingredient.category][ingredient.name] = ingredients_for_all_shopping_recipes[ingredient.category].get(ingredient.name,0)+float(Fraction(ingredient.quantity))
                    else:
                        ingredients_for_all_shopping_recipes[ingredient.category][ingredient.name] = ingredients_for_all_shopping_recipes[ingredient.category].get(ingredient.name,0)
                        
        print("*"*20)
        print(ingredients_for_all_shopping_recipes)

        return render_template("shopping_list.html", logged_in_user =user, shopping_recipes=shopping_recipes,ingredients_for_all_shopping_recipes=ingredients_for_all_shopping_recipes)

####### I think i may not need this route if I have the logic in Jinga???####
@app.route("/add-recipe")
def add_recipe():
    """add a recipe to database"""
    user_email = session.get('logged_in_user_email')
    if not user_email:
        flash("Please login first to add a recipe")
        return redirect('/')
    else:
        # user = crud.get_user_by_email(user_email)
        cuisines = ["American", "British", "Caribbean", "Chinese", "French", "Greek", "Indian", "Italian", "Japanese", "Mediterranean", "Mexican", "Moroccan", "Spanish", "Thai", "Turkish", "Vietnamese", "Food Fusion", "Others"]
        quantity_units = ["tablespoons", "tablespoon", "T", "TB", "Tbl", "Tbsp", 
    "cups","cup","c","C",
    "teaspoons", "teaspoon", "t", "tsp",
    "pints","pint","pt",
    "oz","OZ","ounces","ounce",
    "milliliters","milliliter","ml","mL",
    "liters","liter","L",
    "pounds","pound","LB","lb",
    "a pinch","a dash",
    "gallons","gallon","gl","GL","Gal",
    "kilograms","kilogram","kg",
    "grams","gram","g",
    "","no unit","other unit"]

    return render_template('add_recipe.html', cuisines=cuisines, quantity_units=quantity_units)
        


@app.route("/handle-add-recipe-form", methods=["POST"])
def handle_add_recipe_form():
    """handle user submitted form of newly added recipe. Update database"""
    pass

@app.route("/browse")
def browse_recipes():
    # randomly select 3 cuisines. randomly select 3 recipes per cuisine.
    # {cuisine_type1:[recipe1, recipe2, recipe3], cuisine_type2:[xx,xx,xx], cuisine_type3:[xx,xx,xx]}
    # randomly select 3 courses. randomly select 3 recipes per course.
    # randomly select 3 recipes for Vegetarian and Gluten-free diet.
    # {Vegetarian:[recipe1, recipe2, recipe3], Gluten-free:[xx,xx,xx]}

    some_recipes_3_cuisines = crud.get_some_recipes_3_cuisines()
    some_recipes_3_courses = crud.get_some_recipes_3_courses()
    some_recipes_2_specialdiets = crud.get_some_recipes_2_specialdiets()

    return render_template('browse_homepage.html', some_recipes_3_cuisines=some_recipes_3_cuisines, some_recipes_3_courses=some_recipes_3_courses, some_recipes_2_specialdiets=some_recipes_2_specialdiets)


@app.route("/search", methods=["POST"])
def search():
    """obtain user search input, parse input, and return results"""
    input = request.form.get("search-input") 
    matched_recipes =crud.search_recipes(input)

    user_email = session["logged_in_user_email"]
    current_user = crud.get_user_by_email(user_email)
    # # how to do partial search () e.g. title contains one or multipl words of the input

    # split input (if phrase) to words and then search each word against title, author, ingredient
    # input_list = input.split() # split at space

    # present the results in what order?order by title

    return render_template("search_output.html", current_user=current_user, search_returned_recipes=matched_recipes)

@app.route("/cuisines")
def display_cuisines_homepage():
    allrecipes_allcuisines = crud.get_allrecipes_allcuisines()
    
    return render_template("cuisines.html", allrecipes_allcuisines = allrecipes_allcuisines)

@app.route('/cuisines/<cuisine_type>')
def show_recipes_of_any_cuisine(cuisine_type):
    allrecipes_allcuisines = crud.get_allrecipes_allcuisines()
    recipes_of_the_cuisine_type = allrecipes_allcuisines[cuisine_type]

    user_email = session.get("logged_in_user_email")

    if user_email:
        current_user = crud.get_user_by_email(user_email)
        return render_template("recipes_per_cuisine.html", current_user=current_user,cuisine_type=cuisine_type, recipes_of_the_cuisine_type=recipes_of_the_cuisine_type, allrecipes_allcuisines=allrecipes_allcuisines)
    else:
        return render_template("recipes_per_cuisine.html", cuisine_type=cuisine_type, recipes_of_the_cuisine_type=recipes_of_the_cuisine_type, allrecipes_allcuisines=allrecipes_allcuisines)


@app.route('/specialdiets/<specialdiet_type>')
def show_recipes_of_any_specialdiet(specialdiet_type):
    allrecipes_allspecialdiets = crud.get_allrecipes_allspecialdiets()
    recipes_of_the_specialdiet_type = allrecipes_allspecialdiets[specialdiet_type]

    user_email = session.get("logged_in_user_email")

    if user_email:
        current_user = crud.get_user_by_email(user_email)
        return render_template("recipes_per_specialdiet.html", current_user=current_user,specialdiet_type=specialdiet_type, recipes_of_the_specialdiet_type=recipes_of_the_specialdiet_type, allrecipes_allspecialdiets=allrecipes_allspecialdiets)
    else:
        return render_template("recipes_per_specialdiet.html", specialdiet_type=specialdiet_type, recipes_of_the_specialdiet_type=recipes_of_the_specialdiet_type, allrecipes_allspecialdiets=allrecipes_allspecialdiets)


@app.route('/courses/<course_type>')
def show_recipes_of_any_course(course_type):
    allrecipes_allcourses = crud.get_allrecipes_allcourses()
    recipes_of_the_course_type = allrecipes_allcourses[course_type]

    user_email = session.get("logged_in_user_email")

    if user_email:
        current_user = crud.get_user_by_email(user_email)
        return render_template("recipes_per_course.html", current_user=current_user, course_type=course_type, recipes_of_the_course_type=recipes_of_the_course_type, allrecipes_allcourses=allrecipes_allcourses)
    else:
        return render_template("recipes_per_course.html", course_type=course_type, recipes_of_the_course_type=recipes_of_the_course_type, allrecipes_allcourses=allrecipes_allcourses)




if __name__ == "__main__":
    connect_to_db(app) # connect to your database before app.run gets called, so that Flask can access your database.
    app.run(host="0.0.0.0", debug=True)
