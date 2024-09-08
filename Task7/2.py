# 2.Write a Python program that prompts the user to input two numbers and raises a TypeError exception

try:
    num1=input("Enter the first no:")
    num2 = int(input("Enter the second no:"))
    sum=num1+num2
    print(sum)
except Exception:
    raise TypeError