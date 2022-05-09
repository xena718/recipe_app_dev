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


#create a recipe
with open("data/movies.json") as f:
    recipe_data =json.loads(f.read()) #recipe_data is a python list, converted from json array by loads method

# recipes_in_db =[] 

for recipe in recipe_data:
    title, description, photo_url, servings, prep_time, cook_time, recipe_directions, recipe_ingredients, recipe_cuisine, recipe_course, recipe_specialdiet, note = (
        recipe["title"],
        recipe.get("description",""), 
        recipe["photo_url"],
        recipe["prep_time"],
        recipe["cook_time"],
        recipe["recipe_directions"],
        recipe["recipe_ingredients"],
        recipe["recipe_course"],
        recipe["recipe_specialdiet"],
        recipe.get("note","")
    )
    user = crud.get_user_by_name("cr")
    cuisine = crud.get_cuisine_by_name(recipe_cuisine)

    db_recipe = crud.create_recipe(
        user, title, description, photo_url, servings, 
        prep_time, cook_time, cuisine, note)

    model.db.session.add(db_recipe)
    model.db.session.commit()
    # recipes_in_db.append(db_recipe)
    
    # recipe_directions is a dict 
    
    for key, step_guidance in recipe_directions.items():
        step_number = int(key)
        db_recipe_direction = crud.create_recipe_direction(db_recipe, step_number, step_guidance)
        model.db.session.add(db_recipe_guidance)
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



    
        


#######################sample code from movie rating#############

# Load movie data from JSON file
with open("data/movies.json") as f:
    movie_data = json.loads(f.read())

# Create movies, store them in list so we can use them
# to create fake ratings
movies_in_db = []
for movie in movie_data:
    title, overview, poster_path = (
        movie["title"],
        movie["overview"],
        movie["poster_path"],
    )
    release_date = datetime.strptime(movie["release_date"], "%Y-%m-%d")

    db_movie = crud.create_movie(title, overview, release_date, poster_path)
    movies_in_db.append(db_movie)

model.db.session.add_all(movies_in_db)
model.db.session.commit()

# Create 10 users; each user will make 10 ratings
for n in range(10):
    email = f"user{n}@test.com"  # Voila! A unique email!
    password = "test"

    user = crud.create_user(email, password)
    model.db.session.add(user)

    for _ in range(10):
        random_movie = choice(movies_in_db)
        score = randint(1, 5)

        rating = crud.create_rating(user, random_movie, score)
        model.db.session.add(rating)

model.db.session.commit()
