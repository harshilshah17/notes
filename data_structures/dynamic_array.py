class DynamicArray:
    def __init__(self):
        self.capacity = 1  # initial capacity
        self.length = 0  # current number of elements
        self.arr = [None] * self.capacity  # array to store elements

    def resize(self):
        # double the capacity
        new_capacity = self.capacity * 2
        new_arr = [None] * new_capacity
        # copy elements to the new array
        for i in range(self.length):
            new_arr[i] = self.arr[i]
        self.arr = new_arr
        self.capacity = new_capacity

    def pushback(self, n):
        if self.length == self.capacity:
            self.resize()
        # insert at next empty position
        self.arr[self.length] = n
        self.length += 1

    def get(self, index):
        if 0 <= index < self.length:
            return self.arr[index]
        raise IndexError('Index out of bounds')

    def size(self):
        return self.length

    def __str__(self):
        return str([self.arr[i] for i in range(self.length)])

# Example usage:
dynamic_array = DynamicArray()
dynamic_array.pushback(10)
dynamic_array.pushback(20)
dynamic_array.pushback(30)
print(dynamic_array)  # Output: [10, 20, 30]
print(dynamic_array.get(1))  # Output: 20
print(dynamic_array.size())  # Output: 3
