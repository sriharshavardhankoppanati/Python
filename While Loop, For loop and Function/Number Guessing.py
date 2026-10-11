
import random

# Generate a random number between 1 and 10
secret_number = random.randint(1, 10)

# Set the maximum number of valid guesses
attempts = 3

# Display the game instructions
print("Welcome to the Number Guessing Game!")
print("Guess a number between 1 and 10.")

# Repeat while attempts are available
while attempts > 0:
    # Get the user's guess
    guess = int(input("Guess the number (between 1 and 10): "))

    # Check whether the guess is within the valid range
    if guess < 1 or guess > 10:
        print("Your guess is out of range. Please guess a number between 1 and 10.")
        continue  # Skip the rest of this iteration
    else:
        pass  # No action needed; included to demonstrate pass

    # Reduce attempts only for a valid guess
    attempts -= 1

    # Check whether the guess is correct
    if guess == secret_number:
        print("Congratulations! You guessed the correct number.")
        break  # Exit the loop immediately

    # Give feedback for an incorrect guess
    elif guess > secret_number:
        print("Too high. Try again.")
    else:
        print("Too low. Try again.")

# Execute this else only if the loop ends without break
else:
    print("Better luck next time!")
    print("The correct number was:", secret_number)