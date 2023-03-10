"""
This code read string and non-negative number and display the string
"""
n = int(input("Enter the number of copies: "))
while n <= 0:
    n = int(input("Enter the number of copies: "))

s = input("Enter your string: ")
print(s*n)
