#constant time: following code has a constant time complexity of O(1)
print("Constant time complexity")
i = 0
while i < 11:
    i = i + 1
    print(i)

def add(a, b):
    return a + b

#linear time: following code has a linear time complexity of O(n)
print("Linear time complexity")
n = 10
i = 0
while i < n:
    i = i + 1
    print(i) #f(n) = n

n = 10
i = 0
while i < n:
    i = i + 3
    print(i) #f(n) = n/3

#quadratic time: following code has a quadratic time complexity of O(n^2) (two nested loops)
print("Quadratic time complexity")
def quadratic_example(n):
    for i in range(n):
        for j in range(n):
            print(i, j)

print(quadratic_example(5))

#logarithmic time: following code has a logarithmic time complexity of O(log n) (binary search)
print("Logarithmic time complexity")
def logarithmic_example(n):
    i = 1
    while i < n:
        print(i)
        i *= 2
print(logarithmic_example(10))


#linearithmic time: following code has a linearithmic time complexity of O(n log n) (merge sort)
print("Linearithmic time complexity")
def linearithmic_example(arr):
    def merge_sort(arr):
        if len(arr) > 1:
            mid = len(arr) // 2
            left_half = arr[:mid]
            right_half = arr[mid:]

            merge_sort(left_half)
            merge_sort(right_half)

            i = j = k = 0

            while i < len(left_half) and j < len(right_half):
                if left_half[i] < right_half[j]:
                    arr[k] = left_half[i]
                    i += 1
                else:
                    arr[k] = right_half[j]
                    j += 1
                k += 1

            while i < len(left_half):
                arr[k] = left_half[i]
                i += 1
                k += 1

            while j < len(right_half):
                arr[k] = right_half[j]
                j += 1
                k += 1

    merge_sort(arr)

arr = [38, 27, 43, 3, 9, 82, 10]
linearithmic_example(arr)
print(arr)

#exponential time: following code has an exponential time complexity of O(2^n) (recursive function)
print("Exponential time complexity")
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = 10
print(fibonacci(n))

#factorial time: following code has a factorial time complexity of O(n!) (recursive function)
print("Factorial time complexity")
def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n-1)
print(factorial(5))

