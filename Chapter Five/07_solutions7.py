# -------------------------------------  EXAMPLE ONE -------------------------------------------------

# - Create a function called Greeting.  
# - The function should print "Hello World" and "Good Morning".  
# - Call the function to display the output.  

# SOLUTION
def Greeting():
    print("Hello World")
    print("Good Morning")

Greeting()


# -------------------------------------  EXAMPLE TWO -------------------------------------------------

# - Create another function that prints your name.  
# - Call the function to display your name.  

# SOLUTION
def MyName():
    print("My Name is Ali")
    print("My Age is 50")

MyName()



# -------------------------------------  EXAMPLE THREE -------------------------------------------------

# - Create a function that asks the user to input two numbers.  
# - Calculate the total of the two numbers.  
# - Print the total.  

# SOLUTION
def AddTwoNumbers():
    x = int(input("x: "))
    y = int(input("y: "))
    print("Total:", x + y)

AddTwoNumbers()


# -------------------------------------  EXAMPLE FOUR -------------------------------------------------

# - Create a function called printInfoUser that uses placeholders.  
# - It should take three arguments: name, age, and class.  
# - Print each piece of information in a formatted string.  
# - Call the function with different arguments to test it.  

# SOLUTION
def printInfoUser(name, age, cls):
    print(f"Your name is {name}")
    print(f"Your age is {age}")
    print(f"Your class is {cls}")

printInfoUser("Ahmed", 23, "B4")
printInfoUser("Farhiya", 2, "B5")


# -------------------------------------  EXAMPLE FIVE -------------------------------------------------

# - Create a function called UserInfo that takes two arguments: name and age.  
# - Print the name and age in a formatted string.  
# - Call the function with different names and ages.  

# SOLUTION
def UserInfo(name, age):
    print(f"My Name is {name}")
    print(f"My Age is {age}")

UserInfo("Ahmed", 2)
UserInfo("Aisha", 23)
UserInfo("Saalax", 12)


# -------------------------------------  EXAMPLE SIX -------------------------------------------------

# - Create a function called logIn that takes two arguments: username and password.  
# - If the username is "ahmed" and the password is 123, print "Welcome".  
# - Otherwise, print "Wrong Credentials".  
# - Call the function with different usernames and passwords to test it.  

# SOLUTION
def logIn(username, password):
    if username == "ahmed" and password == 123:
        print("Welcome")
    else:
        print("Wrong Credentials")

logIn("ali", 123121)
logIn("faadumo", 122)
logIn("ahmed", 123)
