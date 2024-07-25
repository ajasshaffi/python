#6.Write a program to check whether given year is leap year or not

yr=int(input("Enter the year: "))

if yr%4==0  or yr%400==0:
    print("Its a leap year")
else:
    print("Its not a leap year")