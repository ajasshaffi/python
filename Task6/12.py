#4.Remove all of the vowels in a string (use string above)

string = "Practice Problems to Drill List Comprehension in Your Head."
vowels=['a','e','i','o','u','A','E','I','O','U']
str1=[i for i in string if i not in vowels]
print(''.join(str1))