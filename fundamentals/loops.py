n = 10
n0 = 0
n1 = 1
x = 0
if n <= 0:
  print("enter positive integer:"n,":")
  print(n0)
else:
  print("number in fibonacci sequence upto", n,":")
  while x < n:
    print(n0, end = ',')
    nth = n0 + n1
    n0 = n1
    n1 = nth
    x += 1
  # output: 0, 1, 1, 2, 3, 5, 8, 13, 21, 34,

# Define a generator function
def even_numbers():
    num = 0
    while num <= 10:
        yield num  # Pauses here and returns num, then resumes next time
        num += 2
# Use the generator
evens = even_numbers()  # This doesn't run the function yet
# Get values one by one
print(next(evens))  # Output: 0
print(next(evens))  # Output: 2
print(next(evens))  # Output: 4
# ... and so on
# Or loop through all
for even in even_numbers():
    print(even)
# Output: 0 2 4 6 8 10

# range vs xrange
numbers = range(1, 6)  # Creates a list: [1, 2, 3, 4, 5]
print("Using range():", list(numbers))  # Prints the full list
print("Memory used by range:", numbers.__sizeof__())  # Shows memory size
numbers_gen = range(1, 6)  # Acts like a generator in Python 3
print("Using xrange-like:", list(numbers_gen))  # Prints: [1, 2, 3, 4, 5]
print("Memory used by xrange-like:", numbers_gen.__sizeof__())  # Less memory
