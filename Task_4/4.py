list1=[1,2,3,4,-1,22,-33,2]
sum=0
for i in list1:
    if i<0:
        continue
    sum+=i
print(sum)