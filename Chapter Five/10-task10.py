# -------------------------------------  EXAMPLE ONE -------------------------------------------------

# - Write a function that calculates the length of a string.  
# - Use a loop to count the number of characters manually.  
# - Alternatively, use the built-in `len()` function for simplicity.  



# -------------------------------------  EXAMPLE TWO -------------------------------------------------

# - Write a function that returns the smaller of two values in manual method
# - Also use min() and See The Difference.  

# SOLUTION
def returnSmallerNumber(a, b, c):
    # Manual comparison method
    # if a < b and a < c:
    #     return a
    # elif b < c:
    #     return b
    # else:
    #     return c

    # Using built-in function
    return min(a, b, c)

result = returnSmallerNumber(10, 5, 8)
print("Smaller number:", result)


# -------------------------------------  EXAMPLE THREE -------------------------------------------------
# - Write a function that returns the smaller of two values in manual method
# - Also use max() and See the Difference.  


def returnLargerNumber(a, b):
    # if a > b:
    #     return a
    # else:
    #     return b

    # Using built-in function 
    return max(a, b)


result = returnLargerNumber(5, 8)
print("Larger number:", result)
