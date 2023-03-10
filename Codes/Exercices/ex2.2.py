"""
This code read 3 integers
and check if 2 of them is equal than the sum 0 else calculate the sum of them
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

sum = 0
if (a == b) or (a == c) or (b == c):
    print(sum)
else :
    sum = a + b + c
    print(sum)
