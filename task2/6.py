password=input("Enter the password: ")
special_characters = set("@$!%*?&")
total_chars=False
is_alpha=False
is_digit=False
upper_case=False
lower_case=False
special_char=False

if len(password)>=8:
    total_chars=True
for char in password:
    if char.isalpha():
        is_alpha=True
        break
for char in password:
    if char.isnumeric():
        is_digit=True
        break
for char in password:
    if char.isupper():
        upper_case=True
        break
for char in password:
    if char.islower():
        lower_case=True
        break
for char in password:
    if char in special_characters:
        special_char = True

if total_chars and is_alpha and is_digit and upper_case and lower_case and special_char:
    print("Is a valid password: ")
else:
    print("Not valid")


