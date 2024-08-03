num=int(input("Enter the number: "))
str1=str(num)
len=len(str1)
sum=0
for digit in str1:
    sum+=int(digit)**len

if sum==num:
    print("Is an Armstrong")
else:
    print("Not an Armstrong")