
# 1.Write a Python program that prompts the user to input an integer and raises a ValueError exception

try:
    num=int(input("Enter  an Integer:"))
except Exception:
    raise ValueError
