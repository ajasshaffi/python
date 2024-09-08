# 3.Write a Python program that executes an operation on a list and handles an IndexError exception
#  if the index is out of range.

try:
    lst1=[1,2,3,4,5]
    print(lst1[88])
except IndexError:
    print("INDEX ERROR")
