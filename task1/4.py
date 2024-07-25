#4.Create a Python program that prompts the user to enter two numbers.
#Compare the numbers using comparison operators (>, <, ==, !=, >=, <=) and print out the result of each comparison.

num1=int(input("Enter the no.1"))
num2=int(input("Enter the no.2"))

if num1==num2:
    print("They are equal")
if num1!=num2:
    print("they are not equal")
if num1>num2:
    print(f'{num1} is greater')
if num1<num2:
    print(f'{num1} is smaller')
if num1>=num2:
    print(f'{num1} is greater or equal')
if num1<=num2:
    print(f'{num1} is greater or equal')