c=3
for i in range(1,8):
    if i % 2 != 0:
        print(" " * c, end=" ")
        c -= 1
        for j in range(i//2+1):
            print(j+1, end="")
        for k in range(i//2, 0,-1):
            print(k, end="")
        print()



for i in range(1,8):
    if i % 2 != 0:
        for j in range(i // 2 + 1):
            print(j + 1, end="")
        print()

for i in range(1,8):
    if i % 2 != 0:
        for k in range(i // 2,0,-1):
            print(k, end="")
        print()