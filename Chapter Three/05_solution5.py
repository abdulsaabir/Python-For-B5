# -------------------------------------  EXAMPLE ONE -------------------------------------------------

# Ask the user to input a number
# Check if the number is even or odd
# Print whether it's odd or even

# SOLUTION
num = int(input("Enter a number: "))
if num % 2 == 0:
    print("It's even")
else:
    print("It's odd")


# -------------------------------------  EXAMPLE TWO -------------------------------------------------

# Define a secret code 'SNU'
# Ask the user to enter the secret code
# Grant permission if the user provides the correct code
# Otherwise, deny permission

# SOLUTION 
secret = 'SNU'
code = input("Enter the secret code: ")
if code == secret:
    print("Permission Granted")
else:
    print("Permission Denied")


# -------------------------------------  EXAMPLE THREE -------------------------------------------------


# Ask the user to enter their age
# If they are younger than 13, tell them they are too young
# If they are younger than 25, tell them they are a boy
# If they are younger than 50, tell them they are a man
# If they are older than 50, tell them they are an adult

# SOLUTION 
age = int(input("Your age: "))
if age < 13:
    print("You are too young")
elif age < 25:
    print("You are a boy")
elif age < 50:
    print("You are a man")
else:
    print("You are an adult")


# -------------------------------------  EXAMPLE FOUR -------------------------------------------------

# Ask the user to input their grade
# Give an A if it's 90 or above 
# Give a B if it's 80 or above 
# Give a C if it's 70 or above
# Otherwise, give a D

# SOLUTION 
points = int(input("Enter your grade: "))
if points >= 90:
    print('A')
elif points >= 80:
    print("B")
elif points >= 70:
    print('C')
else:
    print("D")
