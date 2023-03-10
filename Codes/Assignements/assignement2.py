"""
This code reading a last number of for loop and generate all even numbers
in the range of 1 to n (1..n)
"""

n = int(input("Enter the number of iteration n: "))

for i in range(1,n+1):
    if i % 2 == 0:
        print(i)
