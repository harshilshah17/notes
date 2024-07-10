# Data Structures and Algorithms

## Data Structures
- Singly Linked Lists
- Queues and Stacks
- Doubly Linked Lists
- Binary Search Trees

## Data Types/Data Structures
- **Definition**: A Data Structure (DS) is a way of organizing data so that it can be used effectively.
- **Importance**: Data Types are crucial because they illustrate the kind of value in the variable and tell us what operations can be performed on any particular data.
- **Attribute**: An attribute of data that informs the interpreter on how to classify the variable.
- **Categories in Python**: In Python, there are 4 categories of data types: numerical, sequential, Booleans, and dictionary.
  - **Numeric**: `int`, `float`
  - **Dictionary**: `(key, value)`
  - **Boolean**: `True`, `False`
  - **Sequence Type**: `str`, `list`, `tuple`

### ADT (Abstract Data Types)
- A logical process on how we view data and allowed operations without regard to how it will be implemented.

## Algorithms
- **Definition**: Algorithms are a set of instructions used to solve a problem. Outside of computing, an example of an algorithm would be a recipe from a cookbook to craft a meal; we follow a certain set of instructions from the cookbook to create our meal.

## Data Structures
- **Definition**: DS is a format for accessing, storing, organizing, or structuring data. Overall, it's a technique for how data can inter-relate to each other logically or mathematically.
- **Connection between DS and ADT**: ADT gives us the blueprint while a DS tells us how to implement it.

## Complexity Analysis (Big O)
- **Questions to Consider**:
  - How much time does this algorithm need to finish?
  - How much space does this algorithm need for its computation?

- **Purpose**: Big O gives an upper bound of the complexity in the worst case, helping to quantify performance as the input size becomes arbitrarily large.

### Big O Notation
- **Definition**: O(f(n)), where f(n) is a function that represents the number of operations (steps) that an algorithm performs to solve a problem of size n.
- **Use**: Big-O notation is used to describe the performance or complexity of an algorithm, describing the worst-case scenario in terms of time or space complexity.
- **Parameters**:
  - `n`: The size of the input
- **Complexities ordered from smallest to largest**:
  - **Constant**: O(1)
  - **Logarithmic**: O(log(n))
  - **Linear**: O(n)
  - **Linerithmic**: O(nlog(n))
  - **Quadratic**: O(N²)
  - **Cubic**: O(N³)
  - **Exponential**: O(bⁿ), b > 1
  - **Factorial**: O(n!)

#### Big O Properties
- Different inputs should have different variables O(a + b), a and b arrays nested would be O(a*b).
- Big O doesn't care about constants or multiples. Drop the non-dominant terms.
- Example: Let f be a function that describes the running time of a particular algorithm for an input of size n:
  - `f(n) = 7log(n³) + 15n² + 2n³ + 8`
  - `O(f(n)) = O(n³)`

#### Static Arrays
- Arrays are a way of sorting data contiguously, in some languages, arrays have an allocated size when initialized, this means that the array cannot change after its initialization.


#### Dynamic Arrays
- Dynamic arrays are much more common and useful because of their ability  to be resized, in JS and Python these are default, better to use lists.