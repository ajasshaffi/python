l=int(input("Enter the lower range: "))
u=int(input("Enter the upper range: "))

for i in range(l,u+1):
    for j in range(2,i):
        if i%j==0:
            print(i)
            break


