import random
import timeit
import matplotlib.pyplot as plt
from good_sorts import quicksort, mergesort, heapsort


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