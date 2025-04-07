for i in range(1, 6, 2):
    print(i)

for i in range(5, 0, -1):
    print(i)

i = 1
while i < 6:
    print(i)
    i += 1

i = 5
while i > 0:
    print(i)
    i -= 1

i = 1
while i < 6:
    if i == 3:
        break
    print(i)
    i += 1
else:
    # doesn't invoke work when we have break statement
    print("printing while else")

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print(f"inside while else since {i} reached beyond the while loop limit")

arr = [10, 20, 30, 40, 50]
print(type(arr))
print(arr[4])
arr.append(60)
print(f"after item is added, current array: {arr}")

arr.remove(20)
print(f"after item is removed, current array: {arr}")

arr.insert(2, "AB")
print(f"after item is inserted, current array: {arr}")
for i in arr:
    print(i)

print(len(arr))
for i in range(len(arr), 0, -1):
    print(arr[i - 1])

for index, value in enumerate(arr):
    print(index, value)
