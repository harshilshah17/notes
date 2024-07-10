# Static Array: An array with a fixed size, which cannot be changed once it is created.
print("Static array")
myArray = [1,3,5]
k =int(input("Enter the index of the element you want to access: "))
print(myArray[k], "is the element at index", k)


#Traversal: Accessing each element of the array
print("Traversing the array:")
for i in range(len(myArray)):
   print(myArray[i])

# OR

index = 0
while index < len(myArray):
   print(myArray[index])
   index += 1

#