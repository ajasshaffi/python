#3.Given a string, find the length of the longest substring without repeating characters.

s="malaaayalamariyamo"
max_len=0
print(list(s))
print(set(s))
j=""
str1=""
list1=[]
for i in s:
    if i in j or i in str1:
        list1.append(str1)
        str1=i
        j = ''
    else:
        str1 += i
        j += i
list1.append(str1)



indx1=0
for i in range(len(list1)):
    if len(list1[i])>max_len:
        max_len=len(list1[i])
        indx1=i
print(list1[indx1])


    # if len(str1)>max_len:
    #     max_len=len(str1)
    #     print(max_len)


