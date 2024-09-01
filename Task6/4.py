#4.Write a function that filters names that start with the letter 'A'.
lst1=['Ajas','Rahul']
lst=list(filter(lambda a:a.startswith('A'),lst1))
print(lst)