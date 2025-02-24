import time
import os
from random import randint

# Log decorator
def log(func):
    def wrapper(*args, **kwargs):
        # Record the start time
        start_time = time.time()
        
        # Execute the function
        result = func(*args, **kwargs)
        
        # Record the end time
        end_time = time.time()
        
        # Calculate execution time
        exec_time = round((end_time - start_time) * 1000, 3)  # Time in milliseconds
        
        # Get the current username from environment variables
        username = os.getenv('USER', 'Unknown')
        
        # Log the function details
        with open("machine.log", "a") as log_file:
            log_file.write(f"({username}) Running: {func.__name__.capitalize()} [ exec-time = {exec_time} ms ]\n")
        
        return result
    return wrapper

class CoffeeMachine:
    water_level = 100
    
    @log
    def start_machine(self):
        if self.water_level > 20:
            return True
        else:
            print("Please add water!")
            return False
    
    @log
    def boil_water(self):
        return "boiling..."
    
    @log
    def make_coffee(self):
        if self.start_machine():
            print(self.boil_water())
            print("Coffee is ready!")
    
    @log
    def add_water(self, water_level):
        time.sleep(randint(1, 5))  # Simulate the process of adding water
        self.water_level += water_level
        print("Blub blub blub...")

if __name__ == "__main__":
    machine = CoffeeMachine()
    
    # Making multiple cups of coffee
    for i in range(0, 5):
        machine.make_coffee()
    machine.make_coffee()
    
    # Adding water
    machine.add_water(70)
    
    # Simulate the water level going down
    for _ in range(20):
        time.sleep(0.1)
        machine.water_level -= 1
