#8.Given a list of words, write a program to count the occurrences of each word using a dictionary.

lst=["hello","how","hello",'how']
dct={}

for i in range(len(lst)):
    count = 0
    for j in lst:
        if lst[i]==j:
            count+=1
    dct[lst[i]]=count
print(dct)
