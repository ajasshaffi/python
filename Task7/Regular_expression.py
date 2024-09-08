text ="Lorem ipsum dolor sit amet, consectetur adipiscing elit.Email: john.doe@example.com Phone: (555) 123-4567 Date of Birth: 01-23-1985Lorem ipsum dolor sit amet, consectetur adipiscing elit.Email: alice.smith@example.com Phone: (555) 987-6543 Date of Birth: 05-12-1990)"


# Email Addresses:
# 1.Can you extract all the email addresses mentioned in the text?"
import re
pattern1=re.compile(r"[a-z]+[/.][a-z]+[@][a-z]+[/.]com")
var1=pattern1.findall(text)
print(var1)



# Phone Numbers:
# 2."Using regular expressions, find all the phone numbers mentioned in the text."
pattern2=re.compile(r".\d{3}. \d{3}[-]\d{4}")
var2=pattern2.findall(text)
print(var2)


#Dates of Birth:
#3."Create a regex pattern to extract all the dates of birth from the given text."
pattern3=re.compile(r"\d{2}[-]\d{2}[-]\d{4}")
var3=pattern3.findall(text)
print(var3)



# Full Information for a Specific Person:
# 4."Using regex, can you retrieve the complete information (email, phone, and date of birth) for the person with the email address 'alice.smith@example.com'?"






