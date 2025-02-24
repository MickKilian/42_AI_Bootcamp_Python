# test.py
from datetime import datetime
from recipe import Recipe
from book import Book

def test_recipe():
    print("Testing Recipe class")

    # Create valid Recipe instance
    try:
        spaghetti = Recipe(
            name="Spaghetti Bolognese", 
            cooking_lvl=3, 
            cooking_time=30, 
            ingredients=["spaghetti", "minced meat", "tomato sauce", "garlic"], 
            description="A classic Italian pasta dish.", 
            recipe_type="lunch"
        )
        print(f"Recipe Name: {spaghetti.name}")
        print(f"Cooking Level: {spaghetti.cooking_lvl}")
        print(f"Cooking Time: {spaghetti.cooking_time} minutes")
        print(f"Ingredients: {spaghetti.ingredients}")
        print(f"Description: {spaghetti.description}")
        print(f"Recipe Type: {spaghetti.recipe_type}")
        print(str(spaghetti))

    except ValueError as e:
        print(f"Error: {e}")

    # Create invalid Recipe instance to test validation
    try:
        invalid_recipe = Recipe(
            name="",
            cooking_lvl=6,
            cooking_time=-10,
            ingredients="tomato sauce",
            description="A bad recipe.",
            recipe_type="dinner"
        )
    except ValueError as e:
        print(f"Error: {e}")

def test_book():
    print("\nTesting Book class")

    # Create Book instance
    try:
        my_book = Book("My Recipe Book", datetime.now(), datetime.now())
        print(f"Book Name: {my_book.name}")
        print(f"Created on: {my_book.creation_date}")
        print(f"Last Updated on: {my_book.last_update}")
        print(f"Recipes: {my_book.recipes_list}")
        
        # Add a recipe to the book
        recipe1 = Recipe(
            name="Spaghetti Bolognese", 
            cooking_lvl=3, 
            cooking_time=30, 
            ingredients=["spaghetti", "minced meat", "tomato sauce", "garlic"], 
            description="A classic Italian pasta dish.", 
            recipe_type="lunch"
        )
        my_book.add_recipe(recipe1)
        
        # Print the book with added recipe
        print(f"\nAfter adding a recipe: {my_book}")

    except ValueError as e:
        print(f"Error: {e}")

# Run tests
test_recipe()
test_book()
