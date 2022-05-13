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

# create quantity unit entries for quantity units table
with open("data/quantity-units.json") as f_units:
    units =json.loads(f_units.read())  #units is now a python list

quantity_units_in_db =[]
for unit_name in units:
    quantity_unit = crud.create_quantity_unit (unit_name)
    quantity_units_in_db.append(quantity_unit)

model.db.session.add_all(quantity_units_in_db)
model.db.session.commit()


#create a recipe entry/instance and establish various relationships with recipe
with open("data/recipes.json") as f:
    recipe_data =json.loads(f.read()) #recipe_data is a python list, converted from json array by loads method

# recipes_in_db =[]  

for each_recipe in recipe_data:
    title, author, description, photo_url, servings, prep_time, cook_time, recipe_directions, recipe_ingredients, recipe_cuisine, recipe_courses, recipe_specialdiets, note = (
        each_recipe["title"],
        each_recipe["author"],
        each_recipe.get("description",""), 
        each_recipe["photo_url"],
        each_recipe["servings"],
        each_recipe["prep_time"],
        each_recipe["cook_time"],
        each_recipe["recipe_directions"],
        each_recipe["recipe_ingredients"],
        each_recipe["recipe_cuisine"],
        each_recipe["recipe_courses"],
        each_recipe["recipe_specialdiets"],
        each_recipe.get("note","")
    )

    cuisine = crud.get_cuisine_by_name(recipe_cuisine) #cuisine is an instance

    db_recipe = crud.create_recipe(
        user_cr, title, author, description, photo_url, servings, 
        prep_time, cook_time, cuisine, note) #cuisine is an instance
    
    


    for each_course in recipe_courses:
        course_instance = crud.get_course_by_name(each_course)
        course_instance.recipes.append(db_recipe)    

    for each_specialdiet in recipe_specialdiets:
        specialdiet_instance = crud.get_specialdiet_by_name(each_specialdiet)
        specialdiet_instance.recipes.append(db_recipe) 

    if db_recipe.recipe_id %2 ==0:
        user_cr.shopping_recipes.append(db_recipe) #assication between user and shopping recipes
    else:
        user_cr.saved_recipes.append(db_recipe) #assication between user and saved recipes


    model.db.session.add(db_recipe)
    model.db.session.commit()
    

    # recipe_directions is a dict 
    
    for key, step_guidance in recipe_directions.items():
        step_number = int(key)
        db_recipe_direction = crud.create_recipe_direction(db_recipe, step_number, step_guidance)
        model.db.session.add(db_recipe_direction)
        model.db.session.commit()

    # recipe_ingredients_in_db =[]
    # for recipe_ingredient in recipe_ingredients:
    #     name = recipe_ingredient["name"]
    #     category = recipe_ingredient["category"]
    #     quantity = recipe_ingredient["quantity"]
    #     quantity_unit = recipe_ingredient["unit_name"]

    #     # quantity_unit = crud.get_quantity_unit_by_name(recipe_ingredient["unit_name"])
    #     db_recipe_ingredient = crud.create_recipe_ingredient(db_recipe, name, category,quantity, quantity_unit)
    #     recipe_ingredients_in_db.append(db_recipe_ingredient)
    
    # model.db.session.add_all(recipe_ingredients_in_db)
    # model.db.session.commit()


    recipe_ingredients_in_db =[]
    for recipe_ingredient in recipe_ingredients:
        name = recipe_ingredient["name"]
        category = recipe_ingredient["category"]
        quantity = recipe_ingredient["quantity"]
        # quantity_unit = recipe_ingredient["unit_name"]

        quantity_unit = crud.get_quantity_unit_by_name(recipe_ingredient["unit_name"])
        db_recipe_ingredient = crud.create_recipe_ingredient(db_recipe, name, category,quantity, quantity_unit)
        recipe_ingredients_in_db.append(db_recipe_ingredient)
        model.db.session.add_all(recipe_ingredients_in_db)
        model.db.session.commit()