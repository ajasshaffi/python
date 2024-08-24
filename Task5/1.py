#1.Given a list of integers, write a program to find all the duplicate elements.

lst=[1,1,33,22,54,4,5,4,6,1,6]
set1=set(lst)

lst1=[]
for i in set1:
    count = 0
    for j in lst:
        if i==j:
            count+=1
    if count>1:
        lst1.append(i)
print(lst1)