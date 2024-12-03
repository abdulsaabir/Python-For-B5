# -------------------------------------  EXAMPLE ONE -------------------------------------------------

# - Write a function that calculates the length of a string.  
# - Use a loop to count the number of characters manually.  
# - Alternatively, use the built-in `len()` function for simplicity.  

# SOLUTION
def GetLengthOfString(text):
    # count = 0
    # for i in text:
    #     count += 1
    # return count

    # Using built-in function
    return len(text)

result = GetLengthOfString('2DiojoiuoiuoiuoiSAk')
print(result)



# -------------------------------------  EXAMPLE TWO -------------------------------------------------

# - Demonstrate the use of built-in functions: `max`, `min`, `len`, `round`.  
# - Write a function that returns the smaller of two values using `min()`.  

# SOLUTION
def returnSmallerNumber(a, b):
    # if a < b:
    #     return a
    # else:
    #     return b

    # Using built-in function 
    return min(a, b)


result = returnSmallerNumber(10, 5)
print("Smaller number:", result)


# -------------------------------------  EXAMPLE THREE -------------------------------------------------
def returnLargerNumber(a, b):
    # if a > b:
    #     return a
    # else:
    #     return b

    # Using built-in function 
    return max(a, b)



result = returnLargerNumber(5, 8)
print("Larger number:", result)
