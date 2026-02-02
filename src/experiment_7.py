import timeit
import matplotlib.pyplot as plt

from src.bad_sorts import create_random_list
from src.good_sorts import mergesort, merge


# ************* Experiment 7 *************

def bottom_up_mergesort(L):
    n = len(L)
    window_size = 1
    
    # Iterate through window sizes
    while window_size < n:
        for i in range(0, n, 2 * window_size):
            # Define boundaries for the two sub-lists
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
