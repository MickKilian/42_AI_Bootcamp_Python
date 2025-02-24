# game.py

# Step 1: Define the GotCharacter class
class GotCharacter:
    def __init__(self, first_name=None, is_alive=True):
        self.first_name = first_name
        self.is_alive = is_alive

# Step 2: Define the Stark class that inherits from GotCharacter
class Stark(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        # Call the parent class constructor
        super().__init__(first_name=first_name, is_alive=is_alive)
        
        # Define the attributes specific to the Stark house
        self.family_name = "Stark"
        self.house_words = "Winter is Coming"

    # Method to print the house words
    def print_house_words(self):
        print(f"{self.family_name} House words: {self.house_words}")
        
    # Method to change the is_alive status to False (death)
    def die(self):
        self.is_alive = False
        print(f"{self.first_name} has died.")

# Step 3: Create an instance of the Stark class for Arya
arya = Stark("Arya")

# Step 4: Print the attributes of Arya using __dict__
print(arya.__dict__)

# Step 5: Use the methods
arya.print_house_words()  # Prints House words
arya.die()  # Change is_alive to False and print the death message
print(arya.__dict__)  # Print the updated attributes of Arya

# Example of another character, e.g., Eddard Stark
eddard = Stark("Eddard")

# Print Eddard's attributes
print(eddard.__dict__)

# Step 6: Example of creating another house like Lannister
class Lannister(GotCharacter):
    def __init__(self, first_name=None, is_alive=True):
        super().__init__(first_name=first_name, is_alive=is_alive)
        self.family_name = "Lannister"
        self.house_words = "Hear Me Roar!"

    # Method to print the house words for Lannister
    def print_house_words(self):
        print(f"{self.family_name} House words: {self.house_words}")
        
    # Method to change the is_alive status to False (death) for Lannister
    def die(self):
        self.is_alive = False
        print(f"{self.first_name} has died.")

# Create an instance of the Lannister class for Tyrion
tyrion = Lannister("Tyrion")

# Print Tyrion's attributes
print(tyrion.__dict__)

# Use the methods for Tyrion
tyrion.print_house_words()
tyrion.die()
print(tyrion.__dict__)  # Print the updated attributes of Tyrion
