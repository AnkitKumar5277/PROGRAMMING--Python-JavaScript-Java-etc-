import random
print(random.randint(1,10))

# current Python file ke saare global variables aur functions ka dictionary print karta hai.
a = 10
b = 20
print(globals())
 
# PEP 8 (Coding Style)
def greet_user(name):
    print(f"Hello,{name}!")
def GreetUser(Name):print("Hi",Name)

# Valid identifiers
my_name = "John"
_age = 20
marks1 = 88

a = 10          # int
b = 3.14        # float
c = "Ankit"     # string
d = [1, 2, 3]   # list
e = (4, 5, 6)   # tuple
f = {7, 8, 9}   # set
g = {'name': 'John', 'age': 20}  # dict
h = True        # boolean
i = None        # none

print(x and y)  # False
print(x or y)   # True
print(not x)    # False

s = "Ankit"
print(s[::2])
print(s[::-1])    # tiknA
print(s[:])

set1 = {1, 2, 3}
set2 = {3, 4, 5}
union_set = set1.union(set2)
print("Union of set1 and set2:", union_set)

intersection_set = set1.intersection(set2)
print(intersection_set)

# Function definition
def greet():
    print("Hello! Welcome to Python functions.")

# Function call
greet()

# 🔁 8️⃣ Recursion (Function Calling Itself)
# Concept: Jab ek function apne aap ko call karta hai.
# Example – Factorial using recursion
def factorial(n):
    if n == 1:
        return 1
    else:
        return n * factorial(n -1)
print("factorial of 5 is:", factorial(5))

# 🧠 7️⃣ Return Statement
# Concept: Function se value return karne ke liye use hota hai.
def square(num):
    return num * num
result = square(6)
print("Square is:", result)


# 🧱 9️⃣ Base Condition in Recursion
# Concept: Recursion me base condition stopping point hota hai.
def countdown(n):
    if n==0:
        print("Time's up!")
    else:
        print(n)
        countdown(n-1)
countdown(5)



num1 = 1.5
num2 = 6.3
sum = num1 + num2
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))

num1 = input('Enter first number: ')
num2 = input('Enter second number: ')
sum = float(num1) + float(num2)
print('The sum of {0} and {1} is {2}'.format(num1, num2, sum))
print('The sum is %.1f' %(float(input('Enter first number: ')) + float(input('Enter second number: '))))

kilometers = float(input("Enter value in kilometers: "))
conv_fac = 0.621371
miles = kilometers * conv_fac
print('%0.2f kilometers is equal to %0.2f miles' %(kilometers,miles))

celsius = float(input("Enter: "))
fahrenheit = (celsius * 1.8) + 32
print('%0.1f degree Celsius is equal to %0.1f degree Fahrenheit' %(celsius,fahrenheit))

import random 
print(random.randint(0,9))  #random.randint(a,b)

my_str = "Hello this Is an Example With cased letters"
words = [word.lower() for word in my_str.split()]
words.sort()
print("the sorted words are:")
for word in words:
  print(word)
# # ouput
# The sorted words are:
# an
# cased
# example
# hello
# is
# letters
# this
# with

import cmath
a = 1
b = 5
c = 6
d = (b**2) - (4*a*c)
sol1 = (-b-cmath.sqrt(d))/(2*a)
sol2 = (-b+cmath.sqrt(d))/(2*a)
print('The solution are {0} and {1}'.format(sol1,sol2))
# The solutions are (-3+0j) and (-2+0j)

import cmath  
def solve_quadratic(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)
    return [root1, root2]

x = input('Enter value of x: ')
y = input('Enter value of y: ')
temp = x
x = y
y = temp
print('The value of x after swapping: {}'.format(x))
print('The value of y after swapping: {}'.format(y))

x = 5
y = 10
x, y = y, x
print("x =", x)
print("y =", y)

#Addition and Subtraction
x = x + y
y = x - y
x = x - y
#Multiplication and Division
x = x * y
y = x / y
x = x / y
XOR swap

#This algorithm works for integers only
x = x ^ y
y = x ^ y
x = x ^ y









