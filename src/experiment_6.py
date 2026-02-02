import timeit
import matplotlib.pyplot as plt
import sys

from bad_sorts import create_random_list
from good_sorts import quicksort


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