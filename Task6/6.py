#6.Write a function that filters out palindromic strings from a list.

lst1=['malayalam','ajas','refer']
def palin(string):
    rev=string[::-1]
    if string==rev:
        return True
    else:
        return False

print(list(filter(palin,lst1)))