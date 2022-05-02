"""Models for recipes app."""
from flask_sqlalchemy import SQLAlchemy

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
    author = db.Column(db.String, nullable=False, default="unknown")
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


