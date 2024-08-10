
c=7//2
j=0
for i in range(7):
    if j<=c-1:
        for j in range(i+1):
            print(i+1,end="")
    else:
        for k in range(c,0,-1):
            print(c,end="")
        c-=1
    print()