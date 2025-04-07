str = "Hello"
print(type(str))

print(str[0])  # prints character in first index
print(str[4])  # prints character in fourth index
print(str[0:4])  # prints characters from 0 till 4th index
print(str[:4])  # prints characters from 0 till 4th index
print(str[3:])  # prints characters from 3 till last index
print(str[0:4:2])  # prints chanracters from 0 till 4th index skipping 2 characters
print(str[-1])  # prints last character
print(str[-2])  # prints last 2nd character
print("hello\nhow\nare\nyou")  # \n will make the word to take new line
print(str.upper())
print(str.find("o"))  # prints the index of the character

str2 = "hello how are you"
# prints a list of words separated by space, can use split() with parameters
print(str2.split())

for c in str2:
    print(c)  # prints each character

str3 = ".hello."
print(str3.strip("."))  # prints after removing the starting n trailing specied values

str4 = r"hello\rhey"  # raw string
print(str4)  # prints hello\rhey

str5 = "hello, how are you"
print(str5.count("o"))  # 3

str6 = "I love {}, {} languages"
str7 = "Java"
# print(str6.format(str7))
print(str6.format(str7, ".NET"))

lst = ["c", "cpp", "java"]
print(" ".join(lst)) # prints a space separated string c cpp java

