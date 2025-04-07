# instead of concatinating the string in reverse, we cna use list to store the reverse string and then join as string
str = "Hello, World!"
lst = []
for i in range(len(str) - 1, -1, -1):
    lst.append(str[i])
print("".join(lst))

# syntatic sugar
revlist = [str[i] for i in range(len(str) - 1, -1, -1)]
print("".join(revlist))

# word reverse
wordlist = []
wordsAsString = "Hello how are you"
for word in wordsAsString.split():
    wordlist.append("".join([word[i] for i in range(len(word) - 1, -1, -1)]))

print(" ".join(wordlist))
