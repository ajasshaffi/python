first=0
second=1
list1=[0,1]
for i in range(2,10):
    temp=list1[i-1]+list1[i-2]
    list1.append(temp)
print(list1)

