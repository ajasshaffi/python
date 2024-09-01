#8.Write a function that filters out the prime numbers from a list.

lst1=[1,2,3,4,5,6,7,8,9,10]
def prime(num):
    count=0
    for i in range(1,num//2+1):
        if num%i==0:
            count+=1
    if count>1:
        return False
    else:
        return True
lst2=list(filter(prime,lst1))
print(lst2)