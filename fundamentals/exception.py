# write a program to display a / b where a and b are integers if b = 0, display infinite by handling the zero division error
'''
a = int(input("enter number a : "))
b = int(input("enter number b : "))
try:
  print(a/b)
except:
  print("Infinite")
