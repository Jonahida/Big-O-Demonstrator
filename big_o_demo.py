import random
import time
import matplotlib.pyplot as plt

# Bubble Sort (O(n^2)) - Horrible
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Merge Sort (O(n log n)) - Bad
def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2
        left = arr[:mid]
        right = arr[mid:]

        merge_sort(left)
        merge_sort(right)

        i = j = k = 0

        while i < len(left) and j < len(right):
            if left[i] < right[j]:
                arr[k] = left[i]
                i += 1
            else:
                arr[k] = right[j]
                j += 1
            k += 1

        while i < len(left):
            arr[k] = left[i]
            i += 1
            k += 1

        while j < len(right):
            arr[k] = right[j]
            j += 1
            k += 1

# Naive Fibonacci (O(2^n)) - Horrible
def fibonacci_exp(n):
    if n <= 1:
        return n
    else:
        return fibonacci_exp(n-1) + fibonacci_exp(n-2)

# Factorial (O(n!)) - Horrible
def factorial(n):
    if n == 0 or n == 1:
        return 1
    return n * factorial(n - 1)

# Linear Search (O(n)) - Fair
def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search (O(log n)) - Good
def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    return -1

# Constant Time (O(1)) - Good
def constant_time(arr):
    return arr[0]  # Simply accessing the first element

# Cubic Time (O(n^3)) - Horrible
def cubic_time(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n):
            for k in range(n):
                arr[i] = arr[j] + arr[k]  # Random operation

# Measure time complexity
def measure_time(func, *args):
    start_time = time.time()
    func(*args)
    return time.time() - start_time

# Generate random data
input_sizes = [10, 15, 20, 25, 30, 35]
bubble_sort_times = []
merge_sort_times = []
fibonacci_exp_times = []
factorial_times = []
linear_search_times = []
binary_search_times = []
constant_time_times = []
cubic_time_times = []

for size in input_sizes:
    arr = random.sample(range(size * 10), size)
    
    # Bubble Sort (O(n^2)) - Horrible
    bubble_sort_time = measure_time(bubble_sort, arr.copy())
    bubble_sort_times.append(bubble_sort_time)

    # Merge Sort (O(n log n)) - Bad
    merge_sort_time = measure_time(merge_sort, arr.copy())
    merge_sort_times.append(merge_sort_time)

    # Fibonacci (O(2^n)) - Horrible
    if size <= 20:  # To prevent excessive runtime, limit for larger n
        fibonacci_exp_time = measure_time(fibonacci_exp, size)
        fibonacci_exp_times.append(fibonacci_exp_time)

    # Factorial (O(n!)) - Horrible
    if size <= 10:  # To prevent excessive runtime, limit for larger n
        factorial_time = measure_time(factorial, size)
        factorial_times.append(factorial_time)

    # Linear Search (O(n)) - Fair
    target = random.choice(arr)  # Select a random target value
    linear_search_time = measure_time(linear_search, arr.copy(), target)
    linear_search_times.append(linear_search_time)

    # Binary Search (O(log n)) - Good
    arr_sorted = sorted(arr)
    target = arr_sorted[len(arr_sorted) // 2]  # Use the middle element as the target
    binary_search_time = measure_time(binary_search, arr_sorted, target)
    binary_search_times.append(binary_search_time)

    # Constant Time (O(1)) - Good
    constant_time_time = measure_time(constant_time, arr)
    constant_time_times.append(constant_time_time)

    # Cubic Time (O(n^3)) - Horrible
    cubic_time_time = measure_time(cubic_time, arr.copy())
    cubic_time_times.append(cubic_time_time)

# Plot results
plt.figure(figsize=(10,6))

# Plot only if data is available for the input size
if fibonacci_exp_times:
    plt.plot(input_sizes[:len(fibonacci_exp_times)], fibonacci_exp_times, label="Fibonacci (O(2^n)) - Horrible")

if factorial_times:
    plt.plot(input_sizes[:len(factorial_times)], factorial_times, label="Factorial (O(n!)) - Horrible")

plt.plot(input_sizes, bubble_sort_times, label="Bubble Sort (O(n²)) - Horrible")
plt.plot(input_sizes, cubic_time_times, label="Cubic Time (O(n³)) - Horrible")
plt.plot(input_sizes, merge_sort_times, label="Merge Sort (O(n log n)) - Bad")
plt.plot(input_sizes, linear_search_times, label="Linear Search (O(n)) - Fair")
plt.plot(input_sizes, binary_search_times, label="Binary Search (O(log n)) - Good")
plt.plot(input_sizes, constant_time_times, label="Constant Time (O(1)) - Good")


# Introduction before the table
print("\nThis table displays the execution times (in seconds) for various algorithms and input sizes. "
      "These algorithms represent different time complexities, ranging from constant time (O(1)) to exponential time (O(2^n)).\n")
      
# Create a header for the table-like format
print(f"{'Algorithm':<30} {'Input Size':<15} {'Execution Time (s)'}")
print("-" * 50)

# After the algorithm time table is printed, add a summary with the associated tags
# Print the times for each algorithm with corresponding input size and execution time
for i, size in enumerate(input_sizes):
    print(f"{'Bubble Sort (O(n²))':<30} {size:<15} {bubble_sort_times[i]:.6f}")
    print(f"{'Cubic Time (O(n³))':<30} {size:<15} {cubic_time_times[i]:.6f}")
    print(f"{'Merge Sort (O(n log n))':<30} {size:<15} {merge_sort_times[i]:.6f}")
    print(f"{'Linear Search (O(n))':<30} {size:<15} {linear_search_times[i]:.6f}")
    print(f"{'Binary Search (O(log n))':<30} {size:<15} {binary_search_times[i]:.6f}")
    print(f"{'Constant Time (O(1))':<30} {size:<15} {constant_time_times[i]:.6f}")

    # Only print Fibonacci times if data exists
    if i < len(fibonacci_exp_times):
        print(f"{'Fibonacci (O(2^n))':<30} {size:<15} {fibonacci_exp_times[i]:.6f}")

    # Only print the factorial times if they exist
    if i < len(factorial_times):  # Check if index is valid
        print(f"{'Factorial (O(n!))':<30} {size:<15} {factorial_times[i]:.6f}")

    print("-" * 50)  # Add a line to separate data for each input size

# Add the summary section at the end
print("\nSummary of Time Complexities:")
print("-" * 50)

# Associated tags for each algorithm
tags = {
    "Bubble Sort (O(n²))": "Horrible",
    "Cubic Time (O(n³))": "Horrible",
    "Fibonacci (O(2^n))": "Horrible",
    "Factorial (O(n!))": "Horrible",
    "Merge Sort (O(n log n))": "Bad",
    "Linear Search (O(n))": "Fair",
    "Binary Search (O(log n))": "Good",
    "Constant Time (O(1))": "Good",
}


# Print the sorted dictionary
for algorithm, tag in tags.items():
    print(f"{algorithm:<30} {tag}")


print("-" * 50)  # Separator line after summary


plt.xlabel("Input Size")
plt.ylabel("Time (seconds)")
plt.title("Algorithm Time Complexity Comparison")
plt.legend()
plt.grid(True)
plt.show()

