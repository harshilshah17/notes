# Static Array: An array with a fixed size, which cannot be changed once it is created.
print("Static array")
myArray = [1,3,5,7,9]
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

#Deleting an element from the array by index (delete operation)
print("Deleting an element from the array using the 'del' statement:")
arr = [1, 2, 3, 4, 5]
del arr[2]  # Removes the element at index 2 (which is 3)
print(arr)  # Output: [1, 2, 4, 5]

#Deleting an element from the array by value (remove operation)
print("Deleting an element from the array using the 'remove' method:")
arr = [1, 2, 3, 4, 5]
arr.remove(3)  # Removes the element with the value 3
print(arr)  # Output: [1, 2, 4, 5]

#Deleting an element from the array by index (pop operation)
print("Deleting an element from the array using the 'pop' method:")
arr = [1, 2, 3, 4, 5]
arr.pop(2)  # Removes the element at index 2 (which is 3)
print(arr)  # Output: [1, 2, 4, 5]

#List Comprehension Deleting an element from the array
print("Deleting an element from the array using list comprehension:")
arr = [1, 2, 3, 4, 5]
arr = [x for x in arr if x != 3]  # Removes the element with the value 3
print(arr)  # Output: [1, 2, 4, 5]


#Inserting an element into the array at a specific index
print("Inserting an element into the array:")
arr = [1, 2, 4, 5]
arr.insert(2, 3)  # Inserts the element 3 at index 2
print(arr)  # Output: [1, 2, 3, 4, 5]



