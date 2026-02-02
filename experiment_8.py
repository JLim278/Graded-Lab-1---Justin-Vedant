import timeit
import matplotlib.pyplot as plt

from bad_sorts import insertion_sort, create_random_list
from good_sorts import mergesort, quicksort

# ************* Experiment 8 *************
from bad_sorts import insertion_sort, create_random_list
def experiment8():
    # Experimental parameters
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

        # Use same list for all three algorithms each run
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
