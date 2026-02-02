import sys
import timeit
import matplotlib.pyplot as plt
from src.good_sorts import quicksort, mergesort, heapsort
from src.bad_sorts import create_near_sorted_list

# --- EXPERIMENT 5 ---
def experiment5():
    # Experimental Parameters
    list_length = 2500
    max_value = 10000
    runs = 5
    swaps_list = [0, 1, 2, 5, 10, 25, 50, 100, 250, 500, 1000]

    sys.setrecursionlimit(20000)

    results = {
        "Quick Sort": [],
        "Merge Sort": [],
        "Heap Sort": [],
    }

    print("Starting experiment5")

    for swaps in swaps_list:
        print(f"Testing swaps: {swaps}")

        # Create the near sorted list once per data point then copy inside each test
        base = create_near_sorted_list(list_length, max_value, swaps)
        tests = [
            ("Quick Sort", lambda: quicksort(base.copy())),
            ("Merge Sort", lambda: mergesort(base.copy())),
            ("Heap Sort",  lambda: heapsort(base.copy())),
        ]

        for name, test_func in tests:
            time_taken = timeit.timeit(test_func, number=runs) / runs
            results[name].append(time_taken)

    # Plotting
    plt.figure(figsize=(10, 6))

    for name, times in results.items():
        plt.plot(swaps_list, times, linewidth=1.5, label=name)
    plt.title(f"Experiment 5: swaps vs time")
    plt.xlabel("Number of swaps")
    plt.ylabel("Average Time (sec)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    experiment5()