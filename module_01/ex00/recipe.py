# recipe.py
class Recipe:
    def __init__(self, name, cooking_lvl, cooking_time, ingredients, description, recipe_type):
        # Check if name is a string
        if not isinstance(name, str) or not name:
            raise ValueError("Error: Name must be a non-empty string.")
        
        # Check if cooking_lvl is an integer between 1 and 5
        if not isinstance(cooking_lvl, int) or not (1 <= cooking_lvl <= 5):
            raise ValueError("Error: Cooking level must be an integer between 1 and 5.")
        
        # Check if cooking_time is a non-negative integer
        if not isinstance(cooking_time, int) or cooking_time < 0:
            raise ValueError("Error: Cooking time must be a non-negative integer.")
        
        # Check if ingredients is a list of strings
        if not isinstance(ingredients, list) or not all(isinstance(i, str) for i in ingredients):
            raise ValueError("Error: Ingredients must be a list of strings.")
        
        # Check if recipe_type is valid
        if recipe_type not in ["starter", "lunch", "dessert"]:
            raise ValueError("Error: Recipe type must be 'starter', 'lunch', or 'dessert'.")
        
        # Initialize attributes
        self.name = name
        self.cooking_lvl = cooking_lvl
        self.cooking_time = cooking_time
        self.ingredients = ingredients
        self.description = description
        self.recipe_type = recipe_type

    def __str__(self):
        return f"Recipe name: {self.name}\nLevel: {self.cooking_lvl}\nTime: {self.cooking_time} minutes\nIngredients: {', '.join(self.ingredients)}\nDescription: {self.description if self.description else 'No description provided'}\nType: {self.recipe_type}"
