# -------------------------------------  FUNCTION ONE -------------------------------------------------

# - Write a function that prints numbers from 1 to N.  
# - Call the function with an example value to test it.  

# SOLUTION
def print_numbers_upto(n):
    for i in range(1, n + 1):
        print(i)

print_numbers_upto(19)


# -------------------------------------  FUNCTION TWO -------------------------------------------------

# - Write a function that prints all even numbers from 1 to N.  
# - Use a loop to iterate through numbers and check for evenness.  
# - Call the function with an example value to test it.  

# SOLUTION
def print_even_numbers_upto(n):
    for i in range(2, n + 1, 2):  # Start at 2, increment by 2
        print(i)

print_even_numbers_upto(50)


# -------------------------------------  FUNCTION THREE -------------------------------------------------

# - Write a function that prints the multiplication table for a given number.  
# - Output should display in the format "N x i = result".  
# - Call the function with an example value to test it.  

# SOLUTION
def print_multiplication_table(n):
    for i in range(1, 13):  # Multiplication table up to 12
        print(f'{n} x {i} = {n * i}')

print_multiplication_table(10)


# -------------------------------------  FUNCTION FOUR -------------------------------------------------

# - Write a function that returns the sum of numbers from 1 to N using a `while` loop.  
# - Call the function multiple times, using the returned value as input, and print the results.  

# SOLUTION
def calculate_sum_upto(n):
    total = 0
    current = 1
    while current <= n:
        total += current
        current += 1
    return total

# Test the function
print(calculate_sum_upto(4))  # Output: 10 (1 + 2 + 3 + 4)

x = calculate_sum_upto(4)
print(x)                      # Output: 10

x = calculate_sum_upto(x)
print(x)                      # Output: 55 (sum of numbers from 1 to 10)

x = calculate_sum_upto(x)
print(x)                      # Output: 1540 (sum of numbers from 1 to 55)
