
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
