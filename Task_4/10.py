words=["apple","banana","cherry","date","elderberry0"]
skip_words=["banana","date"]
for i in words:
    if i in skip_words:
        continue
    print(i)