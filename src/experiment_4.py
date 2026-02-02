import sys
import timeit
import matplotlib.pyplot as plt
from src.good_sorts import quicksort, mergesort, heapsort
from src.bad_sorts import create_random_list

# ************* Experiment 4 *************

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


def experiment_4(sizes, max_value=100000, runs=5):
    sys.setrecursionlimit(20000)

    algs = [
        ["quicksort", quicksort],
        ["mergesort", mergesort],
        ["heapsort", heapsort],
    ]

    results = {name: [] for name, _ in algs}

    for n in sizes:
        per = {name: [] for name, _ in algs}

        for _ in range(runs):
            L = create_random_list(n, max_value)

            for name, fn in algs:
                t = time_sort(fn, L)
                per[name].append(t)

        for name in results:
            results[name].append(median(per[name]))

        print(f"n={n} " + " ".join(f"{k}={results[k][-1]:.6f}s" for k in results))

    # Plot
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


if __name__ == "__main__":
    sizes = [500, 1000, 2000, 4000, 8000, 16000]
    experiment_4(sizes)
