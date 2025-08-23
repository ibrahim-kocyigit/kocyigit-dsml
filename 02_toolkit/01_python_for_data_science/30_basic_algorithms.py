# =======================================
# TABLE OF CONTENTS
# =======================================
# 1. What are Algorithms?
# 2. Searching Algorithms
# 3. Sorting Algorithms
# 4. Recursion


# =======================================
# 1. WHAT ARE ALGORITHMS?
# =======================================
# - An algorithm is a step-by-step procedure for solving a problem or accomplishing a task.
# - In programming, we analyze algorithms based on their efficiency, often using "Big O" notation.
# - Big O describes how an algorithm's runtime or space requirements grow as the input size (n) increases.
#   - O(1): Constant time (excellent)
#   - O(log n): Logarithmic time (very good)
#   - O(n): Linear time (good)
#   - O(n^2): Quadratic time (okay for small inputs, bad for large ones)


# =======================================
# 2. SEARCHING ALGORITHMS
# =======================================


# --- Linear Search ---
# - The simplest search. It checks each element one by one.
# - Complexity: O(n) - In the worst case, it has to check the entire list.
def linear_search(data: list, target: int) -> int | None:
    """Returns the index of the target if found, otherwise None."""
    for i in range(len(data)):
        if data[i] == target:
            return i
    return None


# --- Binary Search ---
# - A much faster search algorithm, but with a critical prerequisite:
#   THE LIST MUST BE SORTED.
# - It repeatedly divides the search interval in half.
# - Complexity: O(log n) - Extremely efficient for large datasets.
def binary_search(sorted_data: list, target: int) -> int | None:
    """Returns the index of the target if found, otherwise None."""
    low = 0
    high = len(sorted_data) - 1
    while low <= high:
        mid = (low + high) // 2
        if sorted_data[mid] == target:
            return mid
        elif sorted_data[mid] < target:
            low = mid + 1
        else:
            high = mid - 1
    return None


print("--- Searching Algorithms ---")
my_data = [2, 5, 8, 12, 16, 23, 38, 56, 72]
target_value = 23
print(f"Searching for {target_value} in {my_data}")
print(f"Linear search result (index): {linear_search(my_data, target_value)}")
print(f"Binary search result (index): {binary_search(my_data, target_value)}")
print("-" * 30)


# =======================================
# 3. SORTING ALGORITHMS
# =======================================
# - Note: In practice, always use Python's built-in `list.sort()` or `sorted()`.
#   They are highly optimized (Timsort algorithm, O(n log n)).
# - The following are for educational purposes to understand the logic.


# --- Bubble Sort ---
# - Repeatedly steps through the list, compares adjacent elements, and swaps them if needed.
# - It's simple to understand but very inefficient.
# - Complexity: O(n^2)
def bubble_sort(data: list) -> list:
    """Sorts a list using the bubble sort algorithm."""
    n = len(data)
    # Create a copy to avoid modifying the original list
    sorted_data = data[:]
    for i in range(n):
        # A flag to optimize if the list is already sorted
        swapped = False
        for j in range(0, n - i - 1):
            if sorted_data[j] > sorted_data[j + 1]:
                sorted_data[j], sorted_data[j + 1] = sorted_data[j + 1], sorted_data[j]
                swapped = True
        if not swapped:
            break  # Exit early if no swaps were made in a pass
    return sorted_data


print("--- Sorting Algorithms ---")
unsorted_data = [64, 34, 25, 12, 22, 11, 90]
print(f"Unsorted data: {unsorted_data}")
print(f"Bubble sort result: {bubble_sort(unsorted_data)}")
print("-" * 30)


# =======================================
# 4. RECURSION
# =======================================
# - The process in which a function calls itself to solve a problem.
# - A recursive function must have two parts:
#   1. Base Case: A condition to stop the recursion and prevent an infinite loop.
#   2. Recursive Step: The part where the function calls itself, usually with
#      an argument that moves it closer to the base case.


# --- Example 1: Factorial ---
# - The factorial of n (n!) is the product of all positive integers up to n. (e.g., 5! = 5*4*3*2*1)
def factorial(n: int) -> int:
    """Calculates the factorial of a number using recursion."""
    # Base Case: Factorial of 0 or 1 is 1.
    if n <= 1:
        return 1
    # Recursive Step: n * factorial of (n-1)
    else:
        return n * factorial(n - 1)


# --- Example 2: Fibonacci Sequence ---
# - A sequence where each number is the sum of the two preceding ones (0, 1, 1, 2, 3, 5, 8...).
def fibonacci(n: int) -> int:
    """Finds the n-th Fibonacci number using recursion."""
    # Base Cases
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    # Recursive Step
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)
    # Note: This implementation is very inefficient due to repeated calculations,
    # but it's a classic example of the recursive pattern.


print("--- Recursion ---")
print(f"Factorial of 5 is: {factorial(5)}")
print(f"The 10th Fibonacci number is: {fibonacci(10)}")
print("-" * 30)

print("This concludes the Intermediate Python phase!")

# --- End of File ---
