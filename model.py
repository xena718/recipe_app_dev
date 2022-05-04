"""Models for recipes app."""
from flask_sqlalchemy import SQLAlchemy

import enum
from sqlalchemy import Enum

db = SQLAlchemy()

class User(db.Model):
    """A user."""

    __tablename__ = 'users'

    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String, unique=True, nullable=False)
    user_name = db.Column(db.String, unique=True, nullable=False)
    password = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"user_id = {self.user_id}, email = {self.email}, user_name = {self.user_name}"

class Recipe(db.Modle):
    """A recipe"""

    __tablename__ = "recipes"

    recipe_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.user_id"))
    title = db.Column(db.String(50), nullable=False)
    author = db.Column(db.String, nullable=False)
    description_about = db.Column(db.Text, nullable=True)
    photo_url = db.Column(db.String, nullable=False)
    servings = db.Column(db.Integer, nullable=False)
    prep_time = db.Column(db.String, nullable=False)
    cook_time = db.Column(db.String, nullable=False)
    note = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"recipe title = {self.title}, recipe author = {self.author}"
    
class Saved_Recipe(db.Model):
    """A collection of saved recipe"""

    __tablename__ = "saved_recipes"

    saved_recipes_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    user_id = = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    def __repr__(self):
        return f"recipe id(s) in saved recipe collection = {self.recipe_id}, user id of the recipe collection = {self.user_id}"

class Shopping_List(db.Model):
    """shopping list for added recipes"""

    __tablename__ = "shopping_lists"

    shopping_list_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    user_id = = db.Column(db.Integer, db.ForeignKey("users.user_id"))

    def __repr__(self):
        return f"recipe id(s) in a shopping list = {self.recipe_id}, user id of the shoping list = {self.user_id}"

class Recipe_Direction(db.Model):
    """recipe direction/step"""
    
    ___tablename___ = "recipe_directions"

    direction_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    step_number = db.Column(db.Integer, nullable=False)
    step_guidance = db.Column(db.Text, nullable=False)

    def __repr__(self):
        return f"Cooking directions for recipe id = {self.recipe_id}, step number = {self.step_number}, step guidance = {self.step_guidance}"

class Recipe_Ingredient(db.Model):
    """ingredient for recipe"""

    __tablename__ = "recipe_ingredients"

    recipe_ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.id"))
    quantity = db.Column(db.Integer, nullable=False)
    unit_of_measurement_id = db.Column(db.Integer, db.ForeignKey("units_of_measurement.id"))

    def __repr__(self):
        return f"ingredients for recipe id = {self.recipe_id}, ingredient id = {self.ingredient_id}"

class Ingredient_Category(enum.Enum):
    Baked_and_Bakery = 'Baked and Bakery'
    Beverages = 'Beverages'
    Canned_Goods_and_Soups = 'Canned Goods and Soups'
    Herbs_and_Spices = 'Herbs and Spices'
    Meat_and_Seafood = 'Meat and Seafood'
    Vegetables_and_Fruits = 'Vegetables and Fruits'
    Dairy_Eggs_and_Cheese = 'Dairy Eggs and Cheese'
    Grains_Pasta_and_Sides = 'Grains Pasta and Sides'
    Condiments_and_Seasonings = 'Condiments and Seasonings'
    Basic_Cooking_Ingredients = 'Basic Cooking Ingredients'
    Baking_Supplies = 'Baking Supplies'
    Uncategorized = 'Uncategorized'


class Ingredient (db.Model):
    """ingredient name and category"""

    __tablename__ = 'ingredients'

    ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    category = db.Column(Enum(Ingredient_Category), nullable=False)

    def __repr__(self):
        return f"ingredient id = {self.ingredient_id}, ingredient name = {self.name}, ingredient category = {self.category}"

class Unit_of_Measurement(db.Model):
    """ unit of measurement """

    __tablename__ = 'units_of_measurement'

    unit_of_measurement_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    unit_fullname = db.Column(db.String, nullable=False)
    unit_abbrev = db.Column(db.String, nullable=True)

    def __repr__(self):
        return f"unit full name = {self.unit_fullname}, unit abbreviation = {self.unit_abbrev}"

class Recipe_Category (db.Model):
    """ recipe category """

    __tablename__ = "recipe_categories"

    recipe_category_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    course_id = db.Column(db.Integer, db.ForeignKey("courses.course_id"))
    cuisine_id = db.Column(db.Integer, db.ForeignKey("cuisines.cuisine_id"))
    specialdiet_id = db.Column(db.Integer, db.ForeignKey("specialdiets.specialdiet_id"))

    def __repr__(self):
        return f"recipe id = {self.recipe_id}, course id = {self.course_id}"

class Course (db.Model):
    """ recipe category """

    __tablename__ = "courses"

    course_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"course id = {self.course_id}, course name = {self.name}"

class Cuisine (db.Model):
    """ recipe category """

    __tablename__ = "cuisines"

    cuisine_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"cuisine id = {self.cuisine_id}, cuisine name = {self.name}"

class SpecialDiet (db.Model):
    """ recipe category """

    __tablename__ = "specialdiets"

    specialdiet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)

    def __repr__(self):
        return f"specialdiet id = {self.specialdiet_id}, specialdiet name = {self.name}"