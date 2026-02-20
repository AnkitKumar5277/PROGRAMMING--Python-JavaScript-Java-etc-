# Python Program to Find the Sum of Natural Numbers
num = 16
if num < 0:
   print("Enter a positive number")
else:
   sum = 0
   while(num > 0):
       sum += num
       num -= 1
   print("The sum is", sum)
# The sum is 136

# Write a function to find the sum of first N natural numbers.
# Hint: The formula for the sum of the first N natural numbers is N*(N+1)/2.
# For example, for input 5, the outout should be 15.
def sum_of_natural_numbers(n):
    if n < 1:
        return "Input must be a positive integer."
    return n * (n + 1) // 2  # Using integer division for an exact result
number = 5
result = sum_of_natural_numbers(number)
print(f"The sum of the first {number} natural numbers is {result}.")

# Program to transpose a matrix using a nested loop
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[0,0,0],
         [0,0,0]]
for i in range(len(X)):
   for j in range(len(X[0])):
       result[j][i] = X[i][j]
for r in result:
   print(r)
# [12, 4, 3]
# [7, 5, 8]

''' Program to transpose a matrix using list comprehension'''
X = [[12,7],
    [4 ,5],
    [3 ,8]]
result = [[X[j][i] for j in range(len(X))] for i in range(len(X[0]))]
for r in result:
   print(r)

# Python Program to Find Numbers Divisible by Another Number
my_list = [12, 65, 54, 39, 102, 339, 221,]
# use anonymous function to filter
result = list(filter(lambda x: (x % 13 == 0), my_list))
print("Numbers divisible by 13 are",result)
# Numbers divisible by 13 are [65, 39, 221]

# Write a function to check if a number is divisible by five.
# Return True if the number is divisible by 5. Otherwise, return False.
def is_divisible_by_five(number):
    return number % 5 == 0
# Example usage
print(is_divisible_by_five(10))  # True
print(is_divisible_by_five(12))  # False
print(is_divisible_by_five(0))   # True
print(is_divisible_by_five(-15)) # True

# Factorial of a number using recursion
def recur_factorial(n):
   if n == 1:
       return n
   else:
       return n*recur_factorial(n-1)
num = 7
# check if the number is negative
if num < 0:
   print("Sorry, factorial does not exist for negative numbers")
elif num == 0:
   print("The factorial of 0 is 1")
else:
   print("The factorial of", num, "is", recur_factorial(num))
# The factorial of 7 is 5040

# challenge:
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    elif n == 0 or n == 1:
        return 1
    else:
        result = 1
        for i in range(2, n + 1):
            result *= i
        return result
# Example usage:
number = 5
print(f"The factorial of {number} is {factorial(number)}.")

# Python Program to find the factors of a number
# This function computes the factor of the argument passed
def print_factors(x):
   print("The factors of",x,"are:")
   for i in range(1, x + 1):
       if x % i == 0:
           print(i)
num = 320
print_factors(num)
# The factors of 320 are:
# 1
# 2
# 4
# 5
# 8
# 10
# 16
# 20
# 32
# 40
# 64
# 80
# 160
# 320

# This function adds two numbers
def add(x, y):
    return x + y
# This function subtracts two numbers
def subtract(x, y):
    return x - y
# This function multiplies two numbers
def multiply(x, y):
    return x * y
# This function divides two numbers
def divide(x, y):
    return x / y
print("Select operation.")
print("1.Add")
print("2.Subtract")
print("3.Multiply")
print("4.Divide")
while True:
    # take input from the user
    choice = input("Enter choice(1/2/3/4): ")
    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue
        if choice == '1':
            print(num1, "+", num2, "=", add(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", subtract(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiply(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", divide(num1, num2))
        # check if user wants another calculation
        # break the while loop if answer is no
        next_calculation = input("Let's do next calculation? (yes/no): ")
        if next_calculation == "no":
          break
    else:
        print("Invalid Input")
       # ouput

# Example 3: Using copy() and update()
d1 = {1: 'a', 2: 'b'}
d2 = {2: 'c', 4: 'd'}
d3 = d2.copy()
d3.update(d1)
print(d3)
# {2: 'b', 4: 'd', 1: 'a'}

# Python Program to Shuffle Deck of Cards
# Python program to shuffle a deck of card
# importing modules
import itertools, random
# make a deck of cards
deck = list(itertools.product(range(1,14),['Spade','Heart','Diamond','Club']))
# shuffle the cards
random.shuffle(deck)
# draw five cards
print("You got:")
for i in range(5):
   print(deck[i][0], "of", deck[i][1])
# # ouput
# You got:
# 5 of Heart
# 1 of Heart
# 8 of Spade
# 12 of Spade
# 4 of Spade

# Python Program to Flatten a Nested List
# Example 1: Using List Comprehension
my_list = [[1],[2,3],[4,5,6,7]]
flat_list = [num for sublist in my_list for num in sublist]
print(flat_list)
# [1, 2, 3, 4, 5, 6, 7]

# Example 2: Using Nested for Loops (non pythonic way)
my_list = [[1],[2,3],[4,5,6,7]]
flat_list[]
for sublist in my_list:
  for num in sublist:
    flat_list.append(num)
print(flat_list)
# [1, 2, 3, 4, 5, 6, 7]

