# Using if...elif...else


num = float(input("Enter a number: "))
if num > 0:
   print("Positive number")
elif num == 0:
   print("Zero")
else:
   print("Negative number")

# Using Nested if
num = float(input("Enter a number: "))
if num >= 0:
   if num == 0:
       print("Zero")
   else:
       print("Positive number")
else:
   print("Negative number")
   # Enter a number: 2
# Positive number
# Enter a number: 0
# Zero

# Challenge:
def direction(number):
    if number > 0:
        return 'Up'
    elif number < 0:
        return 'Down'
    else:
        return 'Zero'
# print(direction(5))  # Output: 'Up'

# Python program to check if the input number is odd or even.
# A number is even if division by 2 gives a remainder of 0.
# If the remainder is 1, it is an odd number.
num = int(input("Enter a number: "))
if (num % 2) == 0:
   print("{0} is Even".format(num))
else:
   print("{0} is Odd".format(num))
# Enter a number: 43
# 43 is Odd
# Enter a number: 18
# 18 is Even

# Challenge:
# Write a function to check if the entered integer is odd or even.
def check_odd_or_even(number):
    if number % 2 == 0:
        return "Even"
    else:
        return "Odd"
# Example usage:
print(check_odd_or_even(4))  # Output: Even
print(check_odd_or_even(7))  # Output: Odd

# 2017 is not a leap year
# 1900 is a not leap year
# 2012 is a leap year
# 2000 is a leap year
 
# Python program to check if year is a leap year or not
# To get year (integer input) from the user
year = int(input("Enter a year: "))
if (year % 400 == 0) and (year % 100 == 0):
    print("{0} is a leap year".format(year))
elif (year % 4 ==0) and (year % 100 != 0):
    print("{0} is a leap year".format(year))
else:
    print("{0} is not a leap year".format(year))
# output
# 2000 is a leap year

def count_leap_years(start_year, end_year):
    leap_years = 0
    for year in range(start_year, end_year + 1):
        if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
            leap_years += 1
    return leap_years
print(count_leap_years(2000, 2020))  # Output: 6

# Python program to find the largest number among the three input numbers
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
num3 = float(input("Enter third number: "))
if (num1 >= num2) and (num1 >= num3):
   largest = num1
elif (num2 >= num1) and (num2 >= num3):
   largest = num2
else:
   largest = num3
print("The largest number is", largest)
# The largest number is 14

# ```python
def find_smallest(a, b, c):
    return min(a, b, c)
print(find_smallest(3, 1, 2))  # Output: 1
# ```
