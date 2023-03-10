"""
This code display all integers in the list and display the sum of them
and the max value in the list
"""

lst = []
n = 0

while n <= 0 :
    n = int(input("Enter the number of list elements: "))

for i in range(0,n):
    e = int(input("Enter the integer n°{0}:".format(i+1)))
    lst.append(e)

m = lst[0]
s = lst[0]

for i in range(1,n):
    if m < lst[i]:
        m = lst[i]

    s += lst[i]

print("The sum of the list is {0}".format(s))
print("The max of the list is {0}".format(m))
