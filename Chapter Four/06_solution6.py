# -------------------------------------  EXAMPLE ONE -------------------------------------------------

# - Create a loop that prints numbers from 1 to 10.  
# - Initialize a count variable to 1.  
# - Use a `while` loop to print the count and increment it until it reaches 10.  

# SOLUTION
count = 1
while count < 11:
    print(count)
    count += 1


# -------------------------------------  EXAMPLE TWO -------------------------------------------------

# - Print "Hello World" three times using a loop.  
# - Initialize a count variable to 0.  
# - Use a `while` loop to print "Hello World" and increment the count until it reaches 3.  

# SOLUTION
count = 0
while count < 3:
    print("Hello World")
    count += 1



# -------------------------------------  EXAMPLE THREE -------------------------------------------------

# - Ask the user to answer with 'y' or 'n'.  
# - Use a `while` loop that continues if the answer is 'y'.  
# - Print "Thanks" each time the user responds with 'y'.  
# - Provide an option to change the answer to 'n' to exit the loop.  

# SOLUTION
ans = input("Enter 'Y' or 'N': ")
while ans == 'y':
    print("Thanks")
    ans = input("Enter 'Y' or 'N': ")


# -------------------------------------  EXAMPLE FOUR -------------------------------------------------

# - Ask the user to input the starting number for the count.  
# - Create a loop that runs for 10 iterations.  
# - Print the starting number on each iteration.  
# - Decrement the starting number after each print.  


# SOLUTION
num = int(input("Start: "))
count = 0
while count < 10:
    print(num)
    count += 1
    num -= 1


# -------------------------------------  EXAMPLE FIVE -------------------------------------------------

# - Ask the user to input the starting number for the loop.  
# - Ask the user to specify how many iterations the loop should execute.  
# - Create a loop that prints numbers from the starting number up to the specified number of iterations.  


# SOLUTION
start = int(input("Start: "))
counter = int(input("Iterations: "))
while counter > 0:
    start += 1
    print(start)
    counter -= 1


# -------------------------------------  EXAMPLE SIX -------------------------------------------------

# - Ask the user to input the starting number for the loop.  
# - Ask the user to input the ending number for the loop.  
# - Print all numbers from the starting number to the ending number.  
# - Implement a loop that increments and prints numbers when the starting number is less than the ending number.  
# - Implement a loop that decrements and prints numbers when the starting number is greater than the ending number.  

# SOLUTION
start = int(input("Start: "))
end = int(input("End: "))

while start < end:
    start += 1
    print(start)
while start > end:
    start -= 1
    print(start)


# -------------------------------------  EXAMPLE SEVEN -------------------------------------------------

# - Ask the user to input the starting number for the loop.  
# - Ask the user to input the ending number for the loop.  
# - Calculate the total of all numbers from the start to the ending number.  
# - Print the total. 
# SOLUTION
start = int(input("Start: "))
end = int(input("End: "))
total = 0
while start < end:
    start += 1
    total += start
print("Total:", total)
