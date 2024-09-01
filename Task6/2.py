#2.Write a function that takes a list of integers and returns a list with only the odd numbers.
lst1=[1,2,3,4,5,6,7,8,9]
def oddd(lst1):
    return [i for i in lst1 if i%2!=0]

print(oddd(lst1))

