"""Models for recipes app."""
from flask_sqlalchemy import SQLAlchemy

import enum
from sqlalchemy import Enum

db = SQLAlchemy()

class Saved_Recipe(db.Model):
    """An association between users and saved recipes"""
    #one user can have multiple saved recipes. One recipe can be saved by multiple users.

    __tablename__ = "saved_recipes"

    saved_recipes_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))

    # recipes = db.relationship("Recipe", secondary = "saved_recipes", backref="users")

    def __repr__(self):
        return f"<recipe id in a saved recipe collection = {self.recipe_id}, user id of the recipe = {self.user_id}>"

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    saved_recipes = db.relationship("Recipe", secondary = "saved_recipes", backref="saved_by_users")
    shopping_recipes = db.relationship("Recipe", secondary = "shopping_recipes", backref="shopping_by_users")
    # noted that different attribute names between Recipe and Saved_Recipe, Recipe and Shopping_List are needed.
    #it errors if recipe as attribute names for the two relationship above.

    def __repr__(self):
        return f"<user_id = {self.user_id}, email = {self.email}, user name = {self.name}>"

class Recipe(db.Model):
    """A recipe"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    added_by_user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String, nullable=False)
    description = db.Column(db.Text, nullable=True)
    photo_url = db.Column(db.String, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    prep_time = db.Column(db.String, nullable=False)
    cook_time = db.Column(db.String, nullable=False)
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisines.cuisine_id"))
    note = db.Column(db.Text, nullable=True)

    added_by_user = db.relationship("User", backref="added_recipes")
    # recipe = db.relationship("Recipe", backref="recipe_directions")
    # recipes = db.relationship("Recipe", secondary = "recipes_courses", backref="courses")
    # recipes = db.relationship("Recipe", backref="cuisine")
    # recipes = db.relationship("Recipe", secondary = "recipes_specialdiets", backref="specialdiets")

    # saved_recipes = db.relationship("Recipe", secondary = "saved_recipes", backref="saved_by_users")
    # shopping_recipes = db.relationship("Recipe", secondary = "shopping_recipes", backref="shopping_by_users")
    # created_recipes = db.relationship("Recipe", secondary = "created_recipes", backref="created_by_user")

    def __repr__(self):
        return f"<recipe title = {self.title}, recipe author = {self.author}>"
    

class Shopping_Recipe (db.Model):
    """An association table for users and recipes added to shopping list"""

    __tablename__ = "shopping_recipes"

    shopping_recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    # recipes = db.relationship("Recipe", secondary = "shopping_recipes", backref="users")

    def __repr__(self):
        return f"<recipe id(s) in a shopping list = {self.recipe_id}, user id of the shoping list = {self.user_id}>"

class Recipe_Direction(db.Model):
    """recipe direction/step"""
    
    ___tablename___ = "recipe_directions"

    direction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    step_number = db.Column(db.Integer, nullable=False)
    step_guidance = db.Column(db.Text, nullable=False)

    recipe = db.relationship("Recipe", backref="recipe_directions")
    #each direction has many steps. one to many relationship

    def __repr__(self):
        return f"<Cooking directions for recipe id = {self.recipe_id}, step number = {self.step_number}, step guidance = {self.step_guidance}>"

class Recipe_Ingredient(db.Model):
    """
    ingredients for recipe.
    one recipe has many ingredients. one to many relationship
    """

    __tablename__ = "recipe_ingredients"

    recipe_ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    ingredient = db.Column(db.Text, nullable=False)
    
    recipe = db.relationship("Recipe", backref="recipe_ingredients")

    def __repr__(self):
        return f"<ingredients for recipe id = {self.recipe_id}, ingredients are {self.ingredient}>"

class Recipe_Course (db.Model):
    """ an association table between recipe and course """

    __tablename__ = "recipes_courses"

    recipe_course_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    recipe_id =db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    course_id =db.Column(db.Integer, db.ForeignKey("courses.course_id"))    

    def __repr__(self):
        return f"<recipe id = {self.recipe_id}, course id = {self.course_id}>"

class Course (db.Model):
    """course """

    __tablename__ = "courses"

    course_id = db.Column(db.Integer, primary_key=True,autoincrement=True)
    name = db.Column(db.String, nullable=False)

    recipes = db.relationship("Recipe", secondary = "recipes_courses", backref="courses")
    #recipe and course has many-many relationship. An association table was created.

    def __repr__(self):
        return f"<course id = {self.course_id}, course name = {self.name}>"

class Cuisine (db.Model):
    """ 
    cuisine type. 
    One recipe has one type of cuisine. 
    one cuisine may belong to many recipes. 
    Because I said so. 
    For recipes that has multiple cuisine types, I will select food fusion (one of the cuisine type)
    """

    __tablename__ = "cuisines"

    cuisine_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    recipes = db.relationship("Recipe", backref="cuisine")

    def __repr__(self):
        return f"<cuisine id = {self.cuisine_id}, cuisine name = {self.name}>"

class Recipe_Specialdiet (db.Model):
    """ an association table between recipe and specialdiet """

    __tablename__ = "recipes_specialdiets"

    recipe_specialdiet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id =db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    specialdiet_id = db.Column(db.Integer, db.ForeignKey("specialdiets.specialdiet_id"))

    # recipes = db.relationship("Recipe", secondary = "recipes_specialdiets", backref="specialdiets")

    def __repr__(self):
        return f"<recipe id = {self.recipe_id}, specialdiet id = {self.specialdiet_id}>"

class Specialdiet (db.Model):
    """ type of specialdiet """

    __tablename__ = "specialdiets"

    
    specialdiet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    recipes = db.relationship("Recipe", secondary = "recipes_specialdiets", backref="specialdiets")

    def __repr__(self):
        return f"<specialdiet id = {self.specialdiet_id}, specialdiet name = {self.name}>"
    

def connect_to_db(flask_app, db_uri="postgresql:///joyrecipes", echo=True):
    flask_app.config["SQLALCHEMY_DATABASE_URI"] = db_uri
    flask_app.config["SQLALCHEMY_ECHO"] = echo
    flask_app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

    db.app = flask_app
    db.init_app(flask_app)

    print("Connected to the db!")


if __name__ == "__main__":
    from server import app

    # Call connect_to_db(app, echo=False) if your program output gets
    # too annoying; this will tell SQLAlchemy not to print out every
    # query it executes.

    connect_to_db(app)