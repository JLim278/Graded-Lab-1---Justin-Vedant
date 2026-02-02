import sys
import timeit
import matplotlib.pyplot as plt
from good_sorts import quicksort, mergesort, heapsort
from bad_sorts import create_near_sorted_list

# --- EXPERIMENT 5 ---
def experiment5():
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

    print("experiment 5")

    for swaps in swaps_list:
        print(f"Testing swaps: {swaps}")

        total_q = 0.0
        total_m = 0.0
        total_h = 0.0

        for _ in range(runs):
            base = create_near_sorted_list(list_length, max_value, swaps)

            A = base.copy()
            start = timeit.default_timer()
            quicksort(A)
            total_q += timeit.default_timer() - start

            A = base.copy()
            start = timeit.default_timer()
            mergesort(A)
            total_m += timeit.default_timer() - start

            A = base.copy()
            start = timeit.default_timer()
            heapsort(A)
            total_h += timeit.default_timer() - start

        results["Quick Sort"].append(total_q / runs)
        results["Merge Sort"].append(total_m / runs)
        results["Heap Sort"].append(total_h / runs)

    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(swaps_list, times, linewidth=1.5, label=name)

    plt.title("Experiment 5: swaps vs time")
    plt.xlabel("Number of swaps")
    plt.ylabel("Average Time (sec)")
    plt.legend()
    plt.grid(True)
    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    experiment5()
