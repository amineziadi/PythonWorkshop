"""
This code is calculating the size of a file called "student.txt"
"""
f = open("student.txt", 'r')

s = 0
for l in f:
    s += len(l)

f.close()

print("The size of student.txt: {0}".format(s))
