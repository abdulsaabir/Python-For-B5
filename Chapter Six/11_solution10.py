# -------------------------------------  EXAMPLE ONE -------------------------------------------------

# - Create a list containing mixed data types (string, float, integer, and nested list).  
# - Print the list.  
# - Print the type of the list.  
# - Create another list and multiply its elements by 4.  

# SOLUTION
numbers = ['a', 'b', 3.14, 4, [1, 2, 3]]
print(numbers)
print(type(numbers))

numbers = [1, 2, 3]
print(numbers * 4)


# -------------------------------------  EXAMPLE TWO -------------------------------------------------

# - Create a list of numbers from 1 to 8.  
# - Iterate through the list and print only the odd numbers.  

# SOLUTION
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
for i in numbers:
    if i % 2 != 0:
        print(i)


# -------------------------------------  EXAMPLE THREE -------------------------------------------------

# - Create a list with numbers from 1 to 5.  
# - Modify the last element of the list.  
# - Print the modified last element.  

# SOLUTION
numbers = [1, 2, 3, 4, 5]
numbers[-1] = 'not a number'
print(numbers[-1])


# -------------------------------------  EXAMPLE FOUR -------------------------------------------------

# - Create two lists.  
# - Concatenate the two lists and add additional elements to the resulting list.  
# - Print the new list.  

# SOLUTION
list1 = [1, 2, 3]
list2 = [4, 5, 6]
list3 = list1 + list2
print(list3)


# -------------------------------------  EXAMPLE FIVE -------------------------------------------------
# - Create a list of letters.  
# - Perform slicing to print specific ranges of letters.  

# SOLUTION
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']

# Print from c to e
print(letters[2:5])

# Print from a to d
print(letters[:4])

# Print from d to f
print(letters[3:6])

# Print from f to h
print(letters[5:])


# -------------------------------------  EXAMPLE SIX -------------------------------------------------

# - Check if an item exists in a list.  
# - Print a message based on whether the item is found or not.  

# SOLUTION
numbers = [1, 2, 3, 4, 5]
num = 12
if num not in numbers:
    print("The item is not among the list")
else:
    print("The item is present")
