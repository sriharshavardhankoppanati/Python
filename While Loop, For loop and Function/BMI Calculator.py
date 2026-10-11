# Define a function to calculate BMI
def calculate_bmi(weight, height):
    # Calculate BMI using the given formula
    bmi = weight / (height ** 2)

    # Return the calculated BMI
    return bmi


# Get the user's weight in kilograms
weight = float(input("Enter your weight in kg: "))

# Get the user's height in meters
height = float(input("Enter your height in meters: "))

# Validate the inputs before calculating BMI
if weight > 0 and height > 0:
    # Call the function and store the returned value
    bmi = calculate_bmi(weight, height)

    # Display BMI rounded to two decimal places
    print(f"Your BMI is: {bmi:.2f}")
else:
    print("Please enter a valid positive weight and height.")