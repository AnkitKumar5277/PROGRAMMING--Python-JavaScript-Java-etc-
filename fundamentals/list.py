# list comprehension
l = ["13", "16", "1", "5", "8"]
l = [int(x) for x in l] 
l.sort()                
print(l)                
# Output: [1, 5, 8, 13, 16]

# shallow copy aur deep copy ka difference
import copy
# Original list
original = [1, 2, [3, 4]]
# Shallow copy
shallow_copy = copy.copy(original)
# Deep copy
deep_copy = copy.deepcopy(original)
# Modify the nested list in the original
original[2][0] = 99
print("Original:", original)         # Output: [1, 2, [99, 4]]
print("Shallow copy:", shallow_copy) # Output: [1, 2, [99, 4]] (nested list is affected)
print("Deep copy:", deep_copy)       # Output: [1, 2, [3, 4]] (nested list is unchanged)

# map function
# Define a function to square a number
def square(num):
    return num * num
# List of numbers
numbers = [1, 2, 3, 4, 5]
# Use map() to apply square function to each number
squared_numbers = list(map(square, numbers))
# Print the result
print(squared_numbers)  # Output: [1, 4, 9, 16, 25]
