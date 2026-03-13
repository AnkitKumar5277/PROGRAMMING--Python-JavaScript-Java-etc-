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

# Example: Filter even numbers from a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8]
# Define a function to check if a number is even
def is_even(num):
    return num % 2 == 0
# Use filter() to get only even numbers
even_numbers = list(filter(is_even, numbers))
print(even_numbers)  # Output: [2, 4, 6, 8]

# reduce
from functools import reduce
# Example 1: Sum all numbers in a list
numbers = [1, 2, 3, 4]
result = reduce(lambda x, y: x + y, numbers)
print(result)  # Output: 10 (1+2+3+4)
# Example 2: Multiply all numbers in a list
result = reduce(lambda x, y: x * y, numbers)
print(result)  # Output: 24 (1*2*3*4)
