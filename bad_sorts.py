"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.
"""
import random
import timeit
import matplotlib.pyplot as plt

# Create a random list length "length" containing whole numbers between 0 and max_value inclusive
def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]


# Creates a near sorted list by creating a random list, sorting it, then doing a random number of swaps
def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L


# I have created this function to make the sorting algorithm code read easier
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]


# ******************* Insertion sort code *******************

# This is the traditional implementation of Insertion Sort.
def insertion_sort(L):
    for i in range(1, len(L)):
        insert(L, i)


def insert(L, i):
    while i > 0:
        if L[i] < L[i-1]:
            swap(L, i-1, i)
            i -= 1
        else:
            return


# This is the optimization/improvement we saw in lecture
def insertion_sort2(L):
    for i in range(1, len(L)):
        insert2(L, i)


def insert2(L, i):
    value = L[i]
    while i > 0:
        if L[i - 1] > value:
            L[i] = L[i - 1]
            i -= 1
        else:
            L[i] = value
            return
    L[0] = value


# ******************* Bubble sort code *******************

# Traditional Bubble sort
def bubble_sort(L):
    for i in range(len(L)):
        for j in range(len(L) - 1):
            if L[j] > L[j+1]:
                swap(L, j, j+1)


# ******************* Selection sort code *******************

# Traditional Selection sort
def selection_sort(L):
    for i in range(len(L)):
        min_index = find_min_index(L, i)
        swap(L, i, min_index)


def find_min_index(L, n):
    min_index = n
    for i in range(n+1, len(L)):
        if L[i] < L[min_index]:
            min_index = i
    return min_index

# --- EXPERIMENT 1 --- 
# Compare runtimes of insertion, bubble and selection sort

def experiment1():
    # Experimental Parameters
    list_lengths = [10, 50, 100, 300, 500, 700, 1000] # List lengths (n)
    runs = 10  # Number of runs to average per data point
    
    # Storage for results
    results = {
        "Bubble Sort": [],
        "Selection Sort": [],
        "Insertion Sort": [],
    }

    print(f"Starting experiment1")

    for n in list_lengths:
        print(f"Testing length: {n}")
        
        # Define the tests
        tests = [
            ("Bubble Sort", lambda: bubble_sort(create_random_list(n, 1000))),
            ("Selection Sort", lambda: selection_sort(create_random_list(n, 1000))),
            ("Insertion Sort", lambda: insertion_sort(create_random_list(n, 1000))),
        ]

        for name, test_func in tests:
            # Time the execution
            time_taken = timeit.timeit(test_func, number=runs) / runs
            results[name].append(time_taken)

    # Plotting the Results
    plt.figure(figsize=(10, 6))
    
    for name, times in results.items():
        plt.plot(list_lengths, times, marker='o', label=name)

    plt.title("Bad Sorting Algorithm Performance")
    plt.xlabel("List Length (n)")
    plt.ylabel("Average Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    experiment1()




# --- Experiment 2 ---
# bubblesort2() implementation 
def bubblesort2(L):
    n = len(L)
    for end in range(n - 1, 0, -1):
        swapped = False
        for j in range(end):
            if L[j] > L[j + 1]:
                swap(L, j, j + 1)
                swapped = True
        if not swapped:
            return

# selectionsort2 implementation
def selection_sort2(L):
    left = 0
    right = len(L) - 1
    while left < right:
        min_i = left
        max_i = left
        for i in range(left, right + 1):
            if L[i] < L[min_i]:
                min_i = i
            if L[i] > L[max_i]:
                max_i = i
        swap(L, left, min_i)
        if max_i == left:
            max_i = min_i
        swap(L, right, max_i)
        left += 1
        right -= 1

def time_sort(sort_fn, L):
    A = L.copy()
    start = timeit.default_timer()
    sort_fn(A)
    return timeit.default_timer() - start

# Bubble: original vs new
def experiment_2_bubble(sizes, max_value, runs, swaps=10, seed=0):
    random.seed(seed)
    orig_times = []
    new_times = []
    for n in sizes:
        t1, t2 = [], []
        for _ in range(runs):
            L = create_near_sorted_list(n, max_value, swaps)
            t1.append(time_sort(bubble_sort, L))
            t2.append(time_sort(bubblesort2, L))

        orig_times.append(sorted(t1)[len(t1) // 2])
        new_times.append(sorted(t2)[len(t2) // 2])
    plt.figure()
    plt.plot(sizes, orig_times, label="bubble_sort")
    plt.plot(sizes, new_times, label="bubblesort2")
    plt.xlabel("List length (n)")
    plt.ylabel("Time (seconds)")
    plt.title(f"Experiment 2: Bubble Sort Comparison (near sorted, swaps={swaps})")
    plt.legend()
    plt.tight_layout()
    plt.show()

# Selection: original vs new 
def experiment_2_selection(sizes, max_value, runs, seed=0):
    random.seed(seed)
    orig_times = []
    new_times = []
    for n in sizes:
        t1, t2 = [], []
        for _ in range(runs):
            L = create_random_list(n, max_value)
            t1.append(time_sort(selection_sort, L))
            t2.append(time_sort(selection_sort2, L))

        orig_times.append(sorted(t1)[len(t1) // 2])
        new_times.append(sorted(t2)[len(t2) // 2])
    plt.figure()
    plt.plot(sizes, orig_times, label="selection_sort")
    plt.plot(sizes, new_times, label="selection_sort2")
    plt.xlabel("List length (n)")
    plt.ylabel("Time (seconds)")
    plt.title("Experiment 2: Selection Sort Comparison (random)")
    plt.legend()
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    sizes = [100, 200, 400, 600, 800, 1000, 1200, 1400, 1600]
    experiment_2_bubble(sizes, max_value=10000, runs=5, swaps=10, seed=0)
    experiment_2_selection(sizes, max_value=10000, runs=5, seed=0)
