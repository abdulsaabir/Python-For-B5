# -------------------------------------  EXAMPLE ONE -------------------------------------------------
# Define a name and ID Variables and assign the values 
# Print both of them in one print using f-string

# SOLUTION
name = 'Hassan'
Id = 23
print(f"Your name is {name} and your ID is {Id}")




# -------------------------------------  EXAMPLE TWO -------------------------------------------------

# Ask the user for preferences LIKE favColor, FavAnimal, FavFood etc..
# Print all information in one print statement using f-string

# SOLUTION
fav_color = input("Enter your favorite color: ")
fav_animal = input("Enter your favorite animal: ")
fav_food = input("Enter your favorite food: ")
print(f"Your favorite color is {fav_color}, your favorite animal is {fav_animal} and your favorite food is {fav_food}.")



# -------------------------------------  EXAMPLE THREE -------------------------------------------------
# Ask the user to input two numbers
# Print the division result with four decimal places

# SOLUTION
x = float(input("Enter the first number (X): "))
y = float(input("Enter the second number (Y): "))
print(f'The result of dividing {x} by {y} is: {x / y:.4f}')
