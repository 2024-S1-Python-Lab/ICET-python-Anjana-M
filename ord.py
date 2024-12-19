s=input("Enter a sentence:");
print(s)
wordList =s.split()
print (wordList)
for i in wordList:
    print(f"{i} occurs {wordList.count(i)}times")
