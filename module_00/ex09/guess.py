import random

def guessing_game():
    # Generate a random number between 1 and 99
    secret_number = random.randint(1, 99)

    
    # Initialize the number of trials
    trials = 0
    
    print("Welcome to the Guessing Game!")
    print("I have chosen a number between 1 and 99. Try to guess it.")
    print("Type 'exit' to quit the game.")
    
    while True:
        user_input = input("Enter your guess: ")
        
        # Check if the user wants to exit
        if user_input.lower() == 'exit':
            print("Thanks for playing! The secret number was", secret_number)
            break
        
        # Validate the input is a number
        if not user_input.isdigit():
            print("Please enter a valid number.")
            continue
        
        guess = int(user_input)
        trials += 1
        
        # Check if the guess is correct
        if guess < secret_number:
            print("Too low! Try again.")
        elif guess > secret_number:
            print("Too high! Try again.")
        else:
            # If the guess is correct, handle first try and special message for 42
            if trials == 1:
                print(f"Wow, you guessed it on the first try! The secret number was {secret_number}.")
            else:
                print(f"Congratulations! You've guessed the number {secret_number} correctly in {trials} trials.")
            
            # Special reference to Douglas Adams if the secret number is 42
            if secret_number == 42:
                print("The answer to the ultimate question of life, the universe, and everything.")
            
            break

if __name__ == "__main__":
    guessing_game()
