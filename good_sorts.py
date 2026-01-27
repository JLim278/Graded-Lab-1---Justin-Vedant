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
    


# ************* Experiment 4 *************
def create_random_list(length, max_value):
    L = []
    for i in range(length):
        L.append(random.randint(0, max_value))
    return L

def time_sort(sort_fn, L):
    A = L.copy()
    start = timeit.default_timer()
    sort_fn(A)
    end = timeit.default_timer()
    return end - start

def median(times):
    times = sorted(times)
    mid = len(times) // 2
    if len(times) % 2 == 1:
        return times[mid]
    else:
        return (times[mid - 1] + times[mid]) / 2

def experiment_4(sizes, max_value=100000, runs=5, seed=0):
    random.seed(seed)
    algs = []
    algs.append(["quicksort", quicksort])
    algs.append(["mergesort", mergesort])
    algs.append(["heapsort", heapsort])

    results = {}
    for alg in algs:
        name = alg[0]
        results[name] = []
    for n in sizes:
        per = {}
        for alg in algs:
            name = alg[0]
            per[name] = []
        for r in range(runs):
            L = create_random_list(n, max_value)

            for alg in algs:
                name = alg[0]
                fn = alg[1]
                t = time_sort(fn, L)
                per[name].append(t)
        # store median time for each algorithm at this n
        for alg in algs:
            name = alg[0]
            m = median(per[name])
            results[name].append(m)

        line = "n=" + str(n) + " "
        for alg in algs:
            name = alg[0]
            line += name + "=" + f"{results[name][-1]:.6f}s "
        print(line)

    # plot results
    plt.figure()
    plt.plot(sizes, results["quicksort"], label="quicksort")
    plt.plot(sizes, results["mergesort"], label="mergesort")
    plt.plot(sizes, results["heapsort"], label="heapsort")
    plt.xlabel("List length (n)")
    plt.ylabel("time (sec)")
    plt.title("Experiment 4: Good Sort runtime comparison")
    plt.legend()
    plt.tight_layout()
    plt.show()
    return results

if __name__ == "__main__":
    sizes = [500, 1000, 2000, 4000, 8000, 16000]
    experiment_4(sizes, max_value=100000, runs=5, seed=0)




# ************* Experiment 5 *************
# Helper functions
def swap(L, i, j):
    L[i], L[j] = L[j], L[i]

def create_random_list(length, max_value):
    return [random.randint(0, max_value) for _ in range(length)]

def create_near_sorted_list(length, max_value, swaps):
    L = create_random_list(length, max_value)
    L.sort()
    for _ in range(swaps):
        r1 = random.randint(0, length - 1)
        r2 = random.randint(0, length - 1)
        swap(L, r1, r2)
    return L

def experiment5():
    sys.setrecursionlimit(20000)

    list_length = 2500
    max_value = 10000
    n_runs = 5
    swaps_list = [0, 1, 2, 5, 10, 25, 50, 100, 250, 500, 1000]

    times_quick = []
    times_merge = []
    times_heap = []

    for swaps in swaps_list:
        sum_quick = 0.0
        sum_merge = 0.0
        sum_heap = 0.0

        for _ in range(n_runs):
            L = create_near_sorted_list(list_length, max_value, swaps)

            A = L.copy()
            start = timeit.default_timer()
            quicksort(A)
            sum_quick += (timeit.default_timer() - start)

            A = L.copy()
            start = timeit.default_timer()
            mergesort(A)
            sum_merge += (timeit.default_timer() - start)

            A = L.copy()
            start = timeit.default_timer()
            heapsort(A)
            sum_heap += (timeit.default_timer() - start)

        times_quick.append(sum_quick / n_runs)
        times_merge.append(sum_merge / n_runs)
        times_heap.append(sum_heap / n_runs)

    plt.figure()
    plt.plot(swaps_list, times_quick, label="quicksort")
    plt.plot(swaps_list, times_merge, label="mergesort")
    plt.plot(swaps_list, times_heap, label="heapsort")
    plt.xlabel("Number of swaps")
    plt.ylabel("time (sec)")
    plt.title(f"Experiment 5: swaps vs time)")
    plt.legend()
    plt.tight_layout()
    plt.show()


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





if __name__ == "__main__":
    experiment6()






# ************* Experiment 8 *************
from bad_sorts import insertion_sort, create_random_list
def experiment8():
    # Experimental parameters (small n)
    list_lengths = [2, 3, 4, 5, 6, 8, 10, 12, 15, 20, 25, 30, 40, 50, 60, 75, 100]
    runs = 300
    max_value = 10000

    results = {
        "Insertion Sort": [],
        "Merge Sort": [],
        "Quick Sort": [],
    }

    print("Starting Experiment 8")

    for n in list_lengths:
        print(f"Testing length: {n}")

        # Use the same list for all three algorithms each run
        total_ins = 0.0
        total_mer = 0.0
        total_qui = 0.0

        for _ in range(runs):
            L = create_random_list(n, max_value)

            A = L.copy()
            start = timeit.default_timer()
            insertion_sort(A)
            total_ins += (timeit.default_timer() - start)

            A = L.copy()
            start = timeit.default_timer()
            mergesort(A)
            total_mer += (timeit.default_timer() - start)

            A = L.copy()
            start = timeit.default_timer()
            quicksort(A)
            total_qui += (timeit.default_timer() - start)

        results["Insertion Sort"].append(total_ins / runs)
        results["Merge Sort"].append(total_mer / runs)
        results["Quick Sort"].append(total_qui / runs)

    # Plotting
    plt.figure(figsize=(10, 6))
    plt.plot(list_lengths, results["Insertion Sort"], linewidth=1.5, label="Insertion Sort")
    plt.plot(list_lengths, results["Merge Sort"], linewidth=1.5, label="Merge Sort")
    plt.plot(list_lengths, results["Quick Sort"], linewidth=1.5, label="Quick Sort")
    plt.title("Experiment 8: Insertion vs Merge vs Quick (in small lists)")
    plt.xlabel("List Length (n)")
    plt.ylabel("Average Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()
    plt.yscale("log")
    

if __name__ == "__main__":
    experiment8()
