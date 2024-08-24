#5.Write a program that finds the unique elements in a list using a set
lst1=[1,2,3,4,2,3]
lst2=[]

for i in lst1:
    if i not in lst2:
        lst2.append(i)
    else:
        lst2.remove(i)
print(lst2)
