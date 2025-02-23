cookbook = {
    "Sandwich": {
        "ingredients": ["ham", "bread", "cheese", "tomatoes"],
        "meal": "lunch",
        "prep_time": 10
    },
    "Cake": {
        "ingredients": ["flour", "sugar", "eggs"],
        "meal": "dessert",
        "prep_time": 60
    },
    "Salad": {
        "ingredients": ["avocado", "arugula", "tomatoes", "spinach"],
        "meal": "lunch",
        "prep_time": 15
    },
}

def print_recipes_names():
    print("Recipes in cookbook:")
    for recipe in cookbook:
        print(f"- {recipe}")

def print_recipe_details(recipe_name):
    if recipe_name in cookbook:
        recipe = cookbook[recipe_name]
        print(f"Recipe for {recipe_name}:")
        print(f"Ingredients: {", ".join(recipe["ingredients"])}")
        print(f"Meal type: {recipe["meal"]}")
        print(f"Preparation time: {recipe["prep_time"]} minutes")
    else:
        print(f"Recipe '{recipe_name}' not found.")

def delete_recipe(recipe_name):
    if recipe_name in cookbook:
        del cookbook[recipe_name]
        print(f"Recipe '{recipe_name}' deleted successfully.")
    else:
        print(f"Recipe '{recipe_name}' not found.")

def add_recipe():
    name = input("Enter the name of the recipe: ")
    ingredients = input("Enter ingredients separated by commas: ").split(",")
    ingredients = [ingredient.strip() for ingredient in ingredients]
    meal = input("Enter the meal type (e.g., lunch, dessert): ")

    while True:
        try:
            prep_time = int(input("Enter preparation time in minutes: "))
            if prep_time < 0:
                print("Preparation time cannot be negative. Try again.")
                continue
            break
        except ValueError:
            print("Invalid input. Please enter a valid number.")
        
    cookbook[name] = {
            "ingredients": ingredients,
            "meal": meal,
            "prep_time": prep_time,
    }
    print(f"Recipe '{name}' added successfully.")

def main():
    while True:
        print("Welcome to the Python Cookbook !")
        print("List of available option:")
        print("1: Add a recipe")
        print("2: Delete a recipe")
        print("3: Print a recipe")
        print("4: Print the cookbook")
        print("5: Quit")

        choice = input("Choose an otpion (1-5): ")
        if choice == "1":
            add_recipe()
        elif choice == "2":
            name = input("Enter the name of the recipe to delete: ")
            delete_recipe(name)
        elif choice == "3":
            name = input("Enter a recipe name: ")
            print_recipe_details(name)
        elif choice == "4":
            print_recipes_names()
        elif choice == "5":
            print("Cookbook closed. Goodbye !")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

main()
