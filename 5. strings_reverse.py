str = "Hello, World!"
reverse = ""
for i in range(len(str), 0, -1):
    reverse += str[i - 1]
print(reverse)

straightstr = "john james mitch"
strlst = straightstr.split()
reversewordelst = []
for i in range(0, len(strlst)):
    word = strlst[i]
    reverseword = ""
    for j in range(len(word), 0, -1):
        reverseword += word[j - 1]
    reversewordelst.append(reverseword)
print(" ".join(reversewordelst))
