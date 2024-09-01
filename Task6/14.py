#6.Use a dictionary comprehension to count the length of each word in a sentence (use string above)


string = "Practice Problems to Drill List Comprehension in Your Head."

dict={(i,len(i)) for i in string.split()}
print(dict)