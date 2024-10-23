# -------------------------------------  EXAMPLE ONE -------------------------------------------------

# Define a number variable and assign a value
# Check if the number is greater than, equal to, or less than 10

# SOLUTION
number = 12
if number > 10:
    print("This number is bigger than 10")
elif number == 10:
    print("This number is 10")
else:
    print("This number is less than 10")

# -------------------------------------  EXAMPLE TWO -------------------------------------------------


# Ask the user to enter any number
# Check if the number is positive or negative or zero

# SOLUTION 
RandomNumber = int(input("Enter any number: "))
if RandomNumber > 0:
    print("This is a positive number")
elif RandomNumber < 0:
    print("This is a negative number")
else:
    print("This is number is Zero")


# -------------------------------------  EXAMPLE THREE -------------------------------------------------

# Ask the user to enter the day of the week
# Check if the input matches 'wed' (for example, assuming today is Wednesday)

# SOLUTION 
day = input("Enter the day: ").lower()
if day == "wed":
    print("It's today")
else:
    print("It's not today")