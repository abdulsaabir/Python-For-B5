# -------------------------------------  EXAMPLE ONE -------------------------------------------------

# - Create a function called PrintName that takes a name as an argument.  
# - The function should print the name in a formatted string.  
# - Call the function with different names to test it.  

# SOLUTION
def PrintName(name):
    print(f'Your Name is {name}')

PrintName("Ahmed")
PrintName("Saciido")
PrintName("Jamiilo")


# -------------------------------------  EXAMPLE TWO -------------------------------------------------

# - Create a function that checks whether a number is even or odd.  
# - Print "Even" if the number is even and "Odd" if it is odd.  
# - Call the function with different numbers to test it.  

# SOLUTION
def isEven(n):
    if n % 2 == 0:
        print(f'{n} is Even')
    else:
        print(f'{n} is Odd')

isEven(12)
isEven(11)


# -------------------------------------  EXAMPLE THREE -------------------------------------------------

# - Create a function that prints the square of a number.  
# - Call the function with different numbers to test it.  

# SOLUTION
def square(n):
    total = n ** 2
    print(total)

square(4)
square(6)


# -------------------------------------  EXAMPLE FOUR -------------------------------------------------

# - Create a function that adds two numbers.  
# - Return the result of the addition.  
# - Print the result after calling the function.  

# SOLUTION
def add(a, b):
    return a + b

print(add(4, 3))
num = add(12, 2)
print(num)


# -------------------------------------  EXAMPLE FIVE -------------------------------------------------

# - Create a function that takes a base number and an exponent.  
# - Return the exponential value of the base raised to the exponent.  
# - Store the result in a variable and print the result.  

# SOLUTION
def exp(base, exponent):
    return base ** exponent

num = exp(3, 4)
print(num)


# -------------------------------------  EXAMPLE SIX -------------------------------------------------

# - Create a function that calculates the total points for three subjects: Python, English, and Arabic.  
# - Return the total sum of the points.  
# - Store the result in a variable and print it.  

# SOLUTION
def TotalPoints(python, eng, arabic):
    total = python + eng + arabic
    return total

python_points = 10
english_points = 8
arabic_points = 7

total_score = TotalPoints(python_points, english_points, arabic_points)
print(f"Total Score: {total_score}")
