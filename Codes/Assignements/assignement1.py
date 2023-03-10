"""
This code is reading 3 numbers and check if there are equal,
print the sum of them 3 times else return the sum of them one time
"""
a = int(input("Enter the first number: "))
b = int(input("Enter the second number: "))
c = int(input("Enter the third number: "))

sum = a + b + c

if (a == b) and (b == c):
    for i in range(0,3):
        print(sum)
else :
    print(sum)
