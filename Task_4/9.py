for i in range(1,11):
    for j in range(1,11):
        if i*j<10:
            continue
    print(i,j)
    break