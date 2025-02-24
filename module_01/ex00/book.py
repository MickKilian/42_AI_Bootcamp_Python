# book.py
from datetime import datetime
from recipe import Recipe

class Book:
    def __init__(self, name, last_update, creation_date, recipes_list=None):
        # Default to an empty dictionary if recipes_list is not provided
        if recipes_list is None:
            recipes_list = {"starter": [], "lunch": [], "dessert": []}

        # Check if name is a non-empty string
        if not isinstance(name, str) or not name:
            raise ValueError("Error: Book name must be a non-empty string.")
        
        # Check if last_update and creation_date are datetime objects
        if not isinstance(last_update, datetime) or not isinstance(creation_date, datetime):
            raise ValueError("Error: Last update and creation date must be datetime objects.")

        # Initialize attributes
        self.name = name
        self.last_update = last_update
        self.creation_date = creation_date
        self.recipes_list = recipes_list

    def __str__(self):
        return f"Book Name: {self.name}\nCreated on: {self.creation_date}\nLast Updated on: {self.last_update}\nRecipes: {self.recipes_list}"

    def add_recipe(self, recipe):
        if not isinstance(recipe, Recipe):
            raise ValueError("Error: Recipe must be an instance of the Recipe class.")
        
        # Update last update time
        self.last_update = datetime.now()
        
        # Add recipe to the appropriate list based on recipe type
        if recipe.recipe_type in self.recipes_list:
            self.recipes_list[recipe.recipe_type].append(recipe)
        else:
            raise ValueError("Error: Invalid recipe type.")
