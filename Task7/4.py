# 4.Write a Python program that executes division and handles an ArithmeticError exception
#  if there is an arithmetic error.

try:
    a=int(input("Enter a divisor"))
    b=int(input("Enter a dividend"))
    div=a/b
    print(div)
except ArithmeticError:
    print("Enter a valid number!")
