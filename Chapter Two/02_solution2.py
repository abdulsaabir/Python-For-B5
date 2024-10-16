# -------------------------------------  EXAMPLE ONE -------------------------------------------------

# Ask The user to Enter his/her name
# print Their Name

# SOLUTION ONE 
name = input('Enter your name: ')
print(name)

# SOLUTION TWO
name = input('Enter your name: ')
print('Your name is', name)

# -------------------------------------  EXAMPLE TWO -------------------------------------------------

# Ask the user to input a random number
# print the random Number on the console

# SOLUTION ONE 
random_number = input('Enter a random number: ')
print(random_number)

# SOLUTION TWO
random_number = input("Enter a random Number: ")
print('The random Number is: ', random_number)

# -------------------------------------  EXAMPLE THREE -------------------------------------------------

# Ask the user to Enter his Id
# Change the string Id to integer
# print the type of the old and new Id 

user_id = input('Enter your ID: ')
user_id_int = int(user_id)
print(type(user_id))
print(type(user_id_int))


# -------------------------------------  EXAMPLE FOUR -------------------------------------------------

# Ask the user to input two numbers x, y
# perform all the four basic operations and print each result

x = int(input('Enter the first number (x): '))
y = int(input('Enter the second number (y): '))

addition = x + y
subtraction = x - y
multiplication = x * y
division = x / y

print('Addition:', addition)
print('Subtraction:', subtraction)
print('Multiplication:', multiplication)
print('Division:', division)


# -------------------------------------  EXAMPLE FIVE -------------------------------------------------

# Ask the user to input three words
# Print the words separated by a '-' separator using the sep argument of print

word1 = input('Enter the first word: ')
word2 = input('Enter the second word: ')
word3 = input('Enter the third word: ')
print(word1, word2, word3, sep='-')
