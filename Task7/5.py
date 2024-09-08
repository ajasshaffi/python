# 5.Write a Python program that executes a list operation and handles an AttributeError exception
#  if the attribute does not exist.

try:
    lst1=[1,2,3,4,5]
    sum=lst1.avg()
    print(sum)
except AttributeError:
    print("Enter a valid attribute")