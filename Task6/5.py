#5.Write a function that doubles only the even numbers in a list.

def eveneven(lst1):
    return [i*2 for i in lst1 if i%2==0]

print(eveneven([1,4,3,5,6,7,2]))
