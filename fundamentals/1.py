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










