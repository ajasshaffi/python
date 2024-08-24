#7.Write a program to compute the sum of all the values in a dictionary.

dct={1:2,2:3,3:4}
sum=0
for i in dct.values():
    sum+=i
print(sum)