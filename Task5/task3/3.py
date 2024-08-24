
for i in range(7):
    if i <=7//2:
        for j in range(4,i,-1):
            print("*",end="")
    else:
        for j in range(7//2,i+1):
            print("*", end="")
    print()


