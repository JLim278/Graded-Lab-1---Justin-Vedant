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

def experiment():
    # Experimental Parameters
    list_lengths = [10, 50, 100, 300, 500, 700, 1000] # List lengths (n)
    runs = 10  # Number of runs to average per data point
    
    # Storage for results
    results = {
        "Bubble Sort": [],
        "Selection Sort": [],
        "Insertion Sort": [],
        "Insertion Sort (Opt)": []
    }

    print(f"Starting experiments (Averaging {runs} runs per length)...")

    for n in list_lengths:
        print(f"Testing length: {n}")
        
        # Define the tests
        tests = [
            ("Bubble Sort", lambda: bubble_sort(create_random_list(n, 1000))),
            ("Selection Sort", lambda: selection_sort(create_random_list(n, 1000))),
            ("Insertion Sort", lambda: insertion_sort(create_random_list(n, 1000))),
            ("Insertion Sort (Opt)", lambda: insertion_sort2(create_random_list(n, 1000)))
        ]

        for name, test_func in tests:
            # Time the execution
            time_taken = timeit.timeit(test_func, number=runs) / runs
            results[name].append(time_taken)

    # --- Plotting the Results ---
    plt.figure(figsize=(10, 6))
    
    for name, times in results.items():
        plt.plot(list_lengths, times, marker='o', label=name)

    plt.title("Sorting Algorithm Performance (Random Lists)")
    plt.xlabel("List Length (n)")
    plt.ylabel("Average Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    experiment()
