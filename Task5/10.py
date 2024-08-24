#10.Write a program to append a single element to a list and then extend the list with another list.

lst=[1,2,3,4,5,6]
lst.append(7)
print(lst)
lst1=[11,22,33,44,55]
lst.extend(lst1)
print(lst)