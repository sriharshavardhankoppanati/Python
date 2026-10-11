# Ask the user to enter a number
number = int(input("Enter the number for which you want the multiplication table: "))

# Generate the multiplication table from 1 to 10
for i in range(1, 11):
    # Calculate the product
    result = number * i

    # Display the multiplication table
    print(number, "x", i, "=", result)