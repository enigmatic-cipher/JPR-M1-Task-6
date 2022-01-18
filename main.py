"""
Given 3 numbers a, b and c as input print the middle number.
Input -> a=10, b=30, c=20
Output -> 20
"""
a = int(input("Enter First Number: "))
b = int(input("Enter Second Number: "))
c = int(input("Enter Third Number: "))
if (a<b<c or c<b<a):
  print(f"Middle Number: {b}")
elif (b<a<c or c<a<b):
  print(f"Middle Number: {a}")
else:
  print(f"Middle Number: {c}")
