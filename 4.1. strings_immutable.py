str = "Hello"
# 'str' object does not support item assignment
# str[2] = "c" # throws an error

# concatination works, since its creating a new memory location for str with the whole concatinated value
print(id(str))
str += "hi"
print(str)
print(id(str))
# both id prints will result in diff memory locations

x = 100
y = x
# prints the same address, since id() is not equivalent to & in C language id(x) is returning the address value in x,
# since x is not a primitive type, its actual value is stored in heap memory location, and address is stored in stack variable (x)
print(id(x), id(y))

x = 200
# x address will differ from the previous
print(id(x))

k = 100
# y & k might have the same address
print(id(k))
