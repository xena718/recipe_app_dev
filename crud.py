"""CRUD operations"""

from model import (db, connect_to_db, Saved_Recipe, User, Recipe, Shopping_Recipe, 
    Recipe_Direction, Quantity_Unit, Recipe_Ingredient,Recipe_Course, Course, Cuisine, Recipe_Specialdiet, Specialdiet)

def create_user(email, name, password):
    """Create and return a new user."""

    user = User(email=email, name=name, password=password)

    return user

def get_user_by_name(name):
    """return user (instance) by name."""

    return User.query.filter(User.name == name).first()

def get_user_by_email(email):
    """return user (instance) by email."""

    return User.query.filter(User.email == email).first()

def create_recipe(
        added_by_user, title, author, description, photo_url, servings, 
        prep_time, cook_time, cuisine, note):
    """Create and return a new recipe."""
    #the argument lines need 4 spaces (an extra level of indentation) to distinguish arguments from the rest
    #cuisine: instance.
    #added_by_user:instance 

    recipe = Recipe(added_by_user=added_by_user,title=title, author = author, description=description, 
            photo_url=photo_url, servings=servings, prep_time=prep_time,
            cook_time=cook_time, cuisine=cuisine, note=note)
    
    return recipe    

def get_recipe_by_recipe_id (recipe_id):
    return Recipe.query.get(recipe_id)

def get_all_recipes():
    return Recipe.query.all()

def recipes_dbjoinedload_cuisines():
    return Recipe.query.options(db.joinedload('cuisine')).all()
    #cuisine is the attribute (relationship between Recipe and Cuisine)

def get_recipes_by_cuisine_id(cuisine_id):
    return Recipe.query.filter(Recipe.cuisine_id == cuisine_id).all()

def get_recipe_by_cuisine_name(cuisine_name):
    # Recipe.query.options(db.joinedload('cuisine')).all()
    return Recipe.query.filter(Recipe.cuisine.name == cuisine_name).all()

def recipes_dbjoinedload_recipe_ingredients():
    return Recipe.query.options(db.joinedload('recipe_ingredients')).all()
    #recipe_ingredients is the attribute (relationship between Recipe and Recipe_Ingredient)

def create_saved_recipe(user, recipe):
    """create and return a saved recipe by a user"""
    #user and recipe are not instances, but id

    saved_recipe = Saved_Recipe(user_id=user, recipe_id=recipe)
    return saved_recipe

# def create_saved_recipe(user, recipe):
#     """create and return a saved recipe by a user"""
#     #user and recipe are instances.

#     saved_recipe = Saved_Recipe(user=user, recipe=recipe)
    
    return saved_recipe
    
def get_saved_recipe_by_recipe_id(recipe_id):

    return Saved_Recipe.query.filter(Saved_Recipe.recipe_id == recipe_id).first()


# def create_shopping_recipe(user, recipe):
#     """create and return a recipe by a user for shopping"""
#     #user and recipe are instances. It doesn't work...

#     shopping_recipe = Shopping_Recipe(user=user, recipe=recipe)
    
#     return shopping_recipe
def create_shopping_recipe(user_id, recipe_id):
    """create a entry of shopping recipe by the logged in user"""

    shopping_recipe = Shopping_Recipe(user_id=user_id, recipe_id=recipe_id)
    
    return shopping_recipe

def get_shopping_recipes_by_user(user_id):
    return Shopping_Recipe.query.filter(Shopping_Recipe.user_id == user_id).all()

def create_recipe_direction(recipe, step_number, step_guidance):
    """create and return a cooking step and guidance for a recipe"""
    #recipe is an instance

    recipe_direction = Recipe_Direction(recipe=recipe, step_number=step_number, step_guidance=step_guidance)

    return recipe_direction

def create_recipe_ingredient(recipe, name, category,quantity, unit):
    """create and return ingredient"""
    #category is from Enum list. how to use it.

    recipe_ingredient = Recipe_Ingredient(recipe=recipe, name=name, category=category, quantity=quantity, unit=unit)
    # recipe= : here the recipe refers to the relationship attribute
    #unit=; here the unit refers to the relationship attribute
    return recipe_ingredient

# def get_ingredient_by_name(name):
#     """return ingredient instance by name"""
#     return Ingredient.query.filter(Ingredient.name == name).first()
def create_quantity_unit (name):
    
    quantity_unit = Quantity_Unit(name=name)

    return quantity_unit

def get_quantity_unit_by_name(name):
    return Quantity_Unit.query.filter(Quantity_Unit.name == name).first()


def create_course(name):
    """create a course entry"""
    course = Course(name=name)
    return course

def get_course_by_name(name):
    """create a course entry"""
    return Course.query.filter(Course.name == name).first()

def create_cuisine(name):
    """create a cuisine"""
    cuisine = Cuisine(name=name)
    return cuisine

def get_cuisine_by_name(name):
    """return a cuisine instance by cuisine name"""
    return Cuisine.query.filter(Cuisine.name == name).first()

def create_specialdiet(name):
    """create a specialdiet"""
    specialdiet = Specialdiet(name=name)
    return specialdiet

def get_specialdiet_by_name(name):
    """create a specialdiet entry"""
    return Specialdiet.query.filter(Specialdiet.name == name).first()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)