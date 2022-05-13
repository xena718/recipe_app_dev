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

    # all_ingredients = db.relationship("Recipe_Ingredient", backref="recipe")

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

class Ingredient_Category(enum.Enum):
    Baked_and_Bakery = "Baked and Bakery"
    Beverages = "Beverages"
    Canned_Goods_and_Soups = "Canned Goods and Soups"
    Herbs_and_Spices = "Herbs and Spices"
    Meat_and_Seafood = "Meat and Seafood"
    Vegetables_and_Fruits = "Vegetables and Fruits"
    Dairy_Eggs_and_Cheese = "Dairy Eggs and Cheese"
    Grains_Pasta_and_Sides = "Grains Pasta and Sides"
    Condiments_and_Seasonings = "Condiments and Seasonings"
    Basic_Cooking_Ingredients = "Basic Cooking Ingredients"
    Baking_Supplies = "Baking Supplies"
    Uncategorized = "Uncategorized"

class Quantity_Unit(db.Model):
    """ unit of measurement """

    __tablename__ = 'quantity_units'

    unit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String, nullable=False)
    #for no unit situation, it will be "None" value.

    def __repr__(self):
        return f"<unit name = {self.name}>"


class Recipe_Ingredient(db.Model):
    """
    ingredients for recipe.
    one recipe has many ingredients. one to many relationship between Recipe and Recipe_Ingredient
    """

    __tablename__ = "recipe_ingredients"

    recipe_ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
    name = db.Column(db.Text, nullable=False)
    # category = db.Column(Enum(Ingredient_Category), nullable=False)
    category = db.Column(db.String, nullable=False)
    quantity = db.Column(db.String, nullable =True)
    quantity_unit = db.Column(db.Integer, db.ForeignKey("quantity_units.unit_id"))

    recipe = db.relationship("Recipe", backref="recipe_ingredients")
    unit = db.relationship("Quantity_Unit", backref="recipe_ingredient")
    #one unit one quantity. one to one relationship

    def __repr__(self):
        return f"<ingredients for recipe id = {self.recipe_id}, ingredient name is {self.name}>"


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




# class Recipe_Ingredient(db.Model):
#     """
#     ingredients for recipe.
#     one recipe has many ingredients. one to many relationship
#     """

#     __tablename__ = "recipe_ingredients"

#     recipe_ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
#     ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.ingredient_id"))
#     quantity = db.Column(db.String, nullable=False) 
#     #quantity in string in order to deal with 2/3 in recipe json file
#     #quantity is an empty string to deal with situations where quantity is not needed. e.g. salt
#     quantity_unit_id = db.Column(db.Integer, db.ForeignKey("quantity_units.unit_id"))
    
#     recipe = db.relationship("Recipe", backref="recipe_ingredients")

#     # recipes = db.relationship("Recipe", backref="recipes_ingredients")
#     # ingredients = db.relationship("Ingredient", backref="recipes_ingredients")
#     # recipe_ingredient = db.relationship("Recipe_Ingredient", backref="quantity_units")

#     def __repr__(self):
#         return f"ingredients for recipe id = {self.recipe_id}, ingredient id = {self.ingredient_id}"

# # class Recipe_Ingredient(db.Model):
# #     """
# #     ingredient for recipe.
# #     Middle table between recipe and ingredients.
# #     establish relationship between recipe and unit_of_measurement
# #     """

# #     __tablename__ = "recipes_ingredients"

# #     recipe_ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
# #     recipe_id = db.Column(db.Integer, db.ForeignKey("recipes.recipe_id"))
# #     ingredient_id = db.Column(db.Integer, db.ForeignKey("ingredients.ingredient_id"))
# #     quantity = db.Column(db.String, nullable=False) 
# #     #quantity in string in order to deal with 2/3 in recipe json file
# #     #quantity is an empty string to deal with situations where quantity is not needed. e.g. salt
# #     quantity_unit_id = db.Column(db.Integer, db.ForeignKey("quantity_units.unit_id"))
    
# #     recipes = db.relationship("Recipe", backref="recipes_ingredients")
# #     ingredients = db.relationship("Ingredient", backref="recipes_ingredients")
# #     # recipe_ingredient = db.relationship("Recipe_Ingredient", backref="quantity_units")

# #     def __repr__(self):
# #         return f"ingredients for recipe id = {self.recipe_id}, ingredient id = {self.ingredient_id}"


# ######
# class Ingredient_Category(enum.Enum):
#     Baked_and_Bakery = "Baked and Bakery"
#     Beverages = "Beverages"
#     Canned_Goods_and_Soups = "Canned Goods and Soups"
#     Herbs_and_Spices = "Herbs and Spices"
#     Meat_and_Seafood = "Meat and Seafood"
#     Vegetables_and_Fruits = "Vegetables and Fruits"
#     Dairy_Eggs_and_Cheese = "Dairy Eggs and Cheese"
#     Grains_Pasta_and_Sides = "Grains Pasta and Sides"
#     Condiments_and_Seasonings = "Condiments and Seasonings"
#     Basic_Cooking_Ingredients = "Basic Cooking Ingredients"
#     Baking_Supplies = "Baking Supplies"
#     Uncategorized = "Uncategorized"


# class Ingredient (db.Model):
#     """ingredient name and category"""

#     __tablename__ = 'ingredients'

#     ingredient_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     name = db.Column(db.String, nullable=False)
#     category = db.Column(Enum(Ingredient_Category), nullable=False)

#     # recipes = db.relationship("Recipe", secondary = "recipes_ingredients", backref="ingredients")
#     recipe_ingredients = db.relationship("Recipe_Ingredient", backref="ingredients")


#     def __repr__(self):
#         return f"ingredient id = {self.ingredient_id}, ingredient name = {self.name}, ingredient category = {self.category}"

# class Quantity_Unit(db.Model):
#     """ unit of measurement """

#     __tablename__ = 'quantity_units'

#     unit_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
#     unit_fullname = db.Column(db.String, nullable=False)
#     unit_fullname_plural = db.Column(db.String, nullable=True)

#     #for no unit situation, it will be an empty string.
#     unit_abbrev = db.Column(db.String, nullable=True)
#     #encforce one abbreviation for each recipe fullname.

#     def __repr__(self):
#         return f"unit full name = {self.unit_fullname}, unit abbreviation = {self.unit_abbrev}"
