num=int(input("Enter the no:"))
i=2
count=0
while i<(num//2)+1:
    if num%i==0:
        count=1
    i+=1

if count==0:
    print("Is a prime no")
else:
    print("Not a prime no")