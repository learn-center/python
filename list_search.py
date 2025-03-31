arr=[10,20,30,40,50]

searchnum=int(input("enter a number to search"))
print(f"Number to search for is: {searchnum}")

for i in range(0,len(arr)):
    if arr[i]==searchnum:
        print(f"{searchnum} found at position {i+1}")
        break
    if i==len(arr)-1:
        print(f"{searchnum} not found")

i=0
while i<len(arr):
    if arr[i]==searchnum:
        print(f"{searchnum} found at position {i+1}")
        break
    i+=1
else:
    print(f"{searchnum} not found")