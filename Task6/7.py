#7.Write a function that takes a list of temperatures in Fahrenheit and converts them to Celsius.

lst=[23,44,65]
def fa_to_ce(f):
    return ((f-32)*(5/9))

lst1=list(map(fa_to_ce,lst))
print(f'{lst1}')