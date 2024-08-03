num=int(input("Enter the no: "))
str1=len(str(num))
arm=0
temp_num=num
while temp_num >0:
    temp = temp_num%10
    arm += temp**str1
    temp_num//=10

if arm==num:
    print("It is Armstrong")
else:
    print("Not Armstrong")
