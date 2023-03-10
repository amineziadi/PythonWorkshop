"""
This code is simulation of simple calculator with basic operations
"""

def calc(a, b, o):
    if o == "+":
        return a + b
    elif o == "-":
        return a - b
    elif o == "*":
        return a * b
    elif o == "/":
        return a / b
    else :
        print("No arithmetic operations found !")

def main():
    a = int(input("Enter the first variable: "))
    b = int(input("Enter the second variable: "))
    o = input("Enter the operation '+','-','*','/' : ")
    print(calc(a,b,o))

main()
