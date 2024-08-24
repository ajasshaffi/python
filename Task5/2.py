#2.Write a function to check if two strings are anagrams of each other

def ang_or_not(str1,str2):
    if len(str1)==len(str2):
        if sorted(str1.lower())==sorted(str2.lower()):
            print(True)
        else:
            print(False)
    else:
        print(False)
ang_or_not("refer","reerF")

