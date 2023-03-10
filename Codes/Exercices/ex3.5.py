"""
This code display an histogram created by a list of integeres
"""

lst = []
n = 0

while n <= 0 :
    n = int(input("Enter the number of list elements: "))

for i in range(0,n):
    e = int(input("Enter the integer n°{0}:".format(i+1)))
    lst.append(e)

for e in lst:
    print("*"*e)
