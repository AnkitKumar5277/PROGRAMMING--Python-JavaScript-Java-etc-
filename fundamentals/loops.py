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
