text_file = open("my_text.txt", "w")
text_file.write("Hello, World!")
text_file.write("\nHow are you?")
text_file.close()


text_file = open("my_text.txt", "w")
text_file.write(
    "Previous content is overridden since we've opened the same file again in write mode. "
)
text_file.close()

text_file = open("my_text.txt", "a")
text_file.write(
    "\nPrevious content will stay since we've opened the same file in append mode."
)
text_file.close()

# text_file = open("my_text.txt", "r")
# str = text_file.read()
# print(str)
# text_file.close()

text_file = open("my_text.txt", "r")
line = text_file.readline()
while line:
    print(line)
    line = text_file.readline()
text_file.close()

import struct

binary_file = open("binaryfile.txt", "wb")
str_value = "hello"
data = struct.pack(f"i{len(str_value)}sf", 1001, str_value.encode("utf-8"), 3.14)
binary_file.write(data)
binary_file.close()


binary_file = open("binaryfile.txt", "rb")
data = binary_file.read()
print(data)
data = struct.unpack(f"i{len(str_value)}sf", data)
print(data)
print(data[0], data[1].decode("utf-8"), data[2])

import csv

csv_file = open("student.csv", "w", newline="")
csvwriter = csv.writer(csv_file)
csvwriter.writerow([1001, "John", 45.34])
csvwriter.writerow([1002, "Steve", 65.56])
csv_file.close()

csv_file = open("student.csv", "r", newline="")
csvreader = csv.reader(csv_file)
for row in csvreader:
    print(row)
csv_file.close()
