"""Script to seed database."""

import os
import json
from random import choice, randint

import crud
import model
import server

os.system("dropdb joyrecipes")
os.system("createdb joyrecipes")
#os.system runs a bash command.

model.connect_to_db(server.app)
model.db.create_all()


#create two users
user_cr = crud.create_user("cr@test.com","cr","cr")
user_dm = crud.create_user("dm@test.com","dm","dm")

model.db.session.add_all([user_cr, user_dm])
model.db.session.commit()


#create all cusine entries for cuisines table
#create all course entries for courses table
#create all specialdiet entries for specialdiets table

with open("data/recipe-categories.json") as f_categories:
    categories_data =json.loads(f_categories.read()) # category_data is a python dict converted from json object by loads metho
    cuisine_names = categories_data["cuisines"] #cuisine_names is a list
    course_names = categories_data["courses"] 
    specialdiet_names = categories_data["specialdiets"]

recipe_categories_in_db = []
for cuisine_name in cuisine_names:
    cuisine = crud.create_cuisine(cuisine_name)
    recipe_categories_in_db.append(cuisine)

for course_name in course_names:
    course = crud.create_course(course_name)
    recipe_categories_in_db.append(course)

for specialdiet_name in specialdiet_names:
    specialdiet = crud.create_specialdiet(specialdiet_name)
    recipe_categories_in_db.append(specialdiet)

model.db.session.add_all(recipe_categories_in_db)
model.db.session.commit()

#create quantity unit entries for quantity units table
with open("data/quantity-units.json") as f_units:
    units =json.loads(f_units.read())  #units is now a python list

quantity_units_in_db =[]
for unit in units:
    for key, values in unit.items(): #values is a dict
        unit_fullname = key
        unit_fullname_plural = values["unit_fullname_plural"]
        for abbrev in values["abbreviation"]:
            unit_abbrev = abbrev
            quantity_unit = crud.create_quantity_unit (unit_fullname, unit_fullname_plural, unit_abbrev)
            quantity_units_in_db.append(quantity_unit)

model.db.session.add_all(quantity_units_in_db)
model.db.session.commit()


#create a recipe
with open("data/recipes.json") as f:
    recipe_data =json.loads(f.read()) #recipe_data is a python list, converted from json array by loads method

# recipes_in_db =[] 

for recipe in recipe_data:
    title, author, description, photo_url, servings, prep_time, cook_time, recipe_directions, recipe_ingredients, recipe_cuisine, recipe_course, recipe_specialdiet, note = (
        recipe["title"],
        recipe["author"],
        recipe.get("description",""), 
        recipe["photo_url"],
        recipe["servings"],
        recipe["prep_time"],
        recipe["cook_time"],
        recipe["recipe_directions"],
        recipe["recipe_ingredients"],
        recipe["recipe_cuisine"],
        recipe["recipe_course"],
        recipe["recipe_specialdiet"],
        recipe.get("note","")
    )
    # user = crud.get_user_by_name("cr")
    cuisine = crud.get_cuisine_by_name(recipe_cuisine)

    db_recipe = crud.create_recipe(
        title, author, description, photo_url, servings, 
        prep_time, cook_time, cuisine, note)

    model.db.session.add(db_recipe)
    model.db.session.commit()
    # recipes_in_db.append(db_recipe)
    
    # recipe_directions is a dict 
    
    for key, step_guidance in recipe_directions.items():
        step_number = int(key)
        db_recipe_direction = crud.create_recipe_direction(db_recipe, step_number, step_guidance)
        model.db.session.add(db_recipe_direction)
        model.db.session.commit()

    # recipe_ingredients is a list of dict.
    ingredients_in_db =[]
    for ingredient_dict in recipe_ingredients:
        if ingredient_dict["name"]:
            continue
        else:  
            name = ingredient_dict["name"]
            category = ingredient_dict["category"]
        
            db_ingredient = crud.create_ingredient(name, category)
            ingredients_in_db.append(db_ingredient)

    model.db.session.add_all(ingredients_in_db)
    model.db.session.commit()

    recipe_ingredients_in_db =[]
    for recipe_ingredient in recipe_ingredients:
        quantity = recipe_ingredient["quantity"] 
        name = recipe_ingredient["name"]
        # recipe = db_recipe
        ingredient = crud.get_ingredient_by_name(name) 
        unit_fullname = recipe_ingredient["quantity_unit_fullname"]
        quantity_unit = crud.get_quantity_unit_by_unit_fullname(unit_fullname)
        # recipe, ingredient, quantity_unit are instances.
        db_recipe_ingredient = crud.create_recipe_ingredient(db_recipe, ingredient, quantity, quantity_unit)
        recipe_ingredients_in_db.append(db_recipe_ingredient)
    
    model.db.session.add_all(recipe_ingredients_in_db)
    model.db.session.commit()

    
        
