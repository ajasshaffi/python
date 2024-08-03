word=input("Enter the word: ")
list1=list(word)
list2=list1[::-1]
word1=''.join(map(str,list2))
print(word1)