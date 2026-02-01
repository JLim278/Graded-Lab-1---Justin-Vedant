"""
This file corresponds to the first graded lab of 2XC3.
Feel free to modify and/or add functions to this file.

In contains traditional implementations for:
1) Quick sort
2) Merge sort
3) Heap sort

Author: Vincent Maccio
"""
import random
import sys
import timeit
import matplotlib.pyplot as plt


# ************ Quick Sort ************
def quicksort(L):
    copy = quicksort_copy(L)
    for i in range(len(L)):
        L[i] = copy[i]


def quicksort_copy(L):
    if len(L) < 2:
        return L
    pivot = L[0]
    left, right = [], []
    for num in L[1:]:
        if num < pivot:
            left.append(num)
        else:
            right.append(num)
    return quicksort_copy(left) + [pivot] + quicksort_copy(right)

# *************************************


# ************ Merge Sort *************

def mergesort(L):
    if len(L) <= 1:
        return
    mid = len(L) // 2
    left, right = L[:mid], L[mid:]

    mergesort(left)
    mergesort(right)
    temp = merge(left, right)

    for i in range(len(temp)):
        L[i] = temp[i]


def merge(left, right):
    L = []
    i = j = 0

    while i < len(left) or j < len(right):
        if i >= len(left):
            L.append(right[j])
            j += 1
        elif j >= len(right):
            L.append(left[i])
            i += 1
        else:
            if left[i] <= right[j]:
                L.append(left[i])
                i += 1
            else:
                L.append(right[j])
                j += 1
    return L

# *************************************

# ************* Heap Sort *************

def heapsort(L):
    heap = Heap(L)
    for _ in range(len(L)):
        heap.extract_max()

class Heap:
    length = 0
    data = []

    def __init__(self, L):
        self.data = L
        self.length = len(L)
        self.build_heap()

    def build_heap(self):
        for i in range(self.length // 2 - 1, -1, -1):
            self.heapify(i)

    def heapify(self, i):
        largest_known = i
        if self.left(i) < self.length and self.data[self.left(i)] > self.data[i]:
            largest_known = self.left(i)
        if self.right(i) < self.length and self.data[self.right(i)] > self.data[largest_known]:
            largest_known = self.right(i)
        if largest_known != i:
            self.data[i], self.data[largest_known] = self.data[largest_known], self.data[i]
            self.heapify(largest_known)

    def insert(self, value):
        if len(self.data) == self.length:
            self.data.append(value)
        else:
            self.data[self.length] = value
        self.length += 1
        self.bubble_up(self.length - 1)

    def insert_values(self, L):
        for num in L:
            self.insert(num)

    def bubble_up(self, i):
        while i > 0 and self.data[i] > self.data[self.parent(i)]:
            self.data[i], self.data[self.parent(i)] = self.data[self.parent(i)], self.data[i]
            i = self.parent(i)

    def extract_max(self):
        self.data[0], self.data[self.length - 1] = self.data[self.length - 1], self.data[0]
        max_value = self.data[self.length - 1]
        self.length -= 1
        self.heapify(0)
        return max_value

    def left(self, i):
        return 2 * (i + 1) - 1

    def right(self, i):
        return 2 * (i + 1)

    def parent(self, i):
        return (i + 1) // 2 - 1

    def __str__(self):
        height = math.ceil(math.log(self.length + 1, 2))
        whitespace = 2 ** height
        s = ""
        for i in range(height):
            for j in range(2 ** i - 1, min(2 ** (i + 1) - 1, self.length)):
                s += " " * whitespace
                s += str(self.data[j]) + " "
            s += "\n"
            whitespace = whitespace // 2
        return s

# *************************************
    




# ************* Experiment 6 *************

def dual_quicksort(L):
    # Base case
    if len(L) < 2:
        return 

    # Base case
    if len(L) == 2:
        if L[0] > L[1]:
            L[0], L[1] = L[1], L[0]
        return

    #Select two pivots and ensure p1 <= p2
    p1, p2 = L[0], L[1]
    if p1 > p2:
        p1, p2 = p2, p1

    left, middle, right = [], [], []
    
    #Partition the rest of the list
    for x in L[2:]:
        if x < p1:
            left.append(x)
        elif x > p2:
            right.append(x)
        else:
            middle.append(x)
            
    #Recursively sort the three parts
    dual_quicksort(left)
    dual_quicksort(middle)
    dual_quicksort(right)
    
    #Reconstruct the list
    sorted_list = left + [p1] + middle + [p2] + right
    for i in range(len(L)):
        L[i] = sorted_list[i]

def experiment6():
    # Experimental Parameters
    list_lengths = [10, 100, 250, 500, 750, 1000, 1250, 1500] 
    runs = 10 
    
    results = {
        "Traditional Quick Sort": [],
        "Dual-Pivot Quick Sort": [],
    }

    # Increase recursion depth
    sys.setrecursionlimit(5000)

    print(f"Starting Experiment 6")

    for n in list_lengths:
        print(f"Testing length: {n}")
        
        # Define the tests
        tests = [
            ("Traditional Quick Sort", lambda: quicksort(create_random_list(n, 10000))),
            ("Dual-Pivot Quick Sort", lambda: dual_quicksort(create_random_list(n, 10000))),
        ]

        for name, test_func in tests:
            time_taken = timeit.timeit(test_func, number=runs) / runs
            results[name].append(time_taken)

    # Plotting
    plt.figure(figsize=(10, 6))
    
    for name, times in results.items():
        marker = 'o' if name == "Traditional Quick Sort" else 's'
        plt.plot(list_lengths, times, marker=marker, label=name)

    plt.title("Quicksort Performance: Traditional vs. Dual Pivot")
    plt.xlabel("List Length (n)")
    plt.ylabel("Average Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()


# ************* Experiment 7 *************

def bottom_up_mergesort(L):
    n = len(L)
    window_size = 1
    
    # Iterate through window sizes
    while window_size < n:
        for i in range(0, n, 2 * window_size):
            # Define boundaries for the two sub-lists
            # Python slicing handles indices out of bounds
            left = L[i : i + window_size]
            right = L[i + window_size : i + 2 * window_size]
            
            # Combine the two sorted segments using your existing merge helper
            merged = merge(left, right)
            
            # Place the merged results back into the original list L
            for j in range(len(merged)):
                L[i + j] = merged[j]
        
        window_size *= 2

def experiment7():
    # Experimental Parameters
    list_lengths = [1000, 2000, 4000, 8000, 16000, 32000] 
    runs = 10 
    
    results = {
        "Traditional Merge Sort": [],
        "Bottom-Up Merge Sort": [],
    }

    print(f"Starting Experiment 7")

    for n in list_lengths:
        print(f"Testing length: {n}")
        
        # Define the tests
        tests = [
            ("Traditional Merge Sort", lambda: mergesort(create_random_list(n, 100000))),
            ("Bottom-Up Merge Sort", lambda: bottom_up_mergesort(create_random_list(n, 100000))),
        ]

        for name, test_func in tests:
            # Time the execution and average across runs
            time_taken = timeit.timeit(test_func, number=runs) / runs
            results[name].append(time_taken)

    # Plotting
    plt.figure(figsize=(10, 6))
    
    for name, times in results.items():
        marker = 'o' if name == "Traditional Merge Sort" else 's'
        plt.plot(list_lengths, times, marker=marker, label=name)

    plt.title("Experiment 7: Traditional vs. Bottom-Up Merge Sort")
    plt.xlabel("List Length (n)")
    plt.ylabel("Average Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    experiment7()
