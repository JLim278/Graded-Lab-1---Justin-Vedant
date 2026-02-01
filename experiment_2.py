import random
import timeit
import matplotlib.pyplot as plt
import bad_sorts as bad


# Experiment 2: bubble variation
# Shift based bubble
def bubblesort2(L):
    n = len(L)
    for end in range(n - 1, 0, -1):
        j = 1
        while j <= end:
            if L[j] >= L[j - 1]:
                j += 1
            else:
                value = L[j]
                k = j
                # shift bigger values right until value belongs
                while k > 0 and L[k - 1] > value:
                    L[k] = L[k - 1]
                    k -= 1
                L[k] = value
                j += 1


# Experiment 2: selection variation
# Track min and max each pass, shrink boundaries
def selectionsort2(L):
    left = 0
    right = len(L) - 1

    while left < right:
        min_i = left
        max_i = left

        for i in range(left, right + 1):
            if L[i] < L[min_i]:
                min_i = i
            if L[i] > L[max_i]:
                max_i = i

        # place min at left
        L[left], L[min_i] = L[min_i], L[left]

        # fix max index if got moved by min swap
        if max_i == left:
            max_i = min_i

        # place max at right
        L[right], L[max_i] = L[max_i], L[right]

        left += 1
        right -= 1


def avg_pair_times(sort_a, sort_b, n, runs, max_value, gen_fn):
    total_a = 0.0
    total_b = 0.0

    for _ in range(runs):
        base = gen_fn(n, max_value)

        a = base.copy()
        start = timeit.default_timer()
        sort_a(a)
        total_a += timeit.default_timer() - start

        b = base.copy()
        start = timeit.default_timer()
        sort_b(b)
        total_b += timeit.default_timer() - start

    return total_a / runs, total_b / runs


# plotting (2 graphs)
def run_experiment2():
    random.seed(0)

    list_lengths = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
    runs = 5
    max_value = 10**6
    swaps = 10

    gen_bubble = lambda n, max_value: bad.create_near_sorted_list(n, max_value, swaps)
    gen_select = bad.create_random_list

    # Bubble vs Bubble2 (near-sorted)
    bubble_times = []
    bubble2_times = []
    for n in list_lengths:
        t1, t2 = avg_pair_times(bad.bubble_sort, bubblesort2, n, runs, max_value, gen_bubble)
        bubble_times.append(t1)
        bubble2_times.append(t2)

    plt.figure()
    plt.plot(list_lengths, bubble_times, marker="o", label="bubble_sort (given)")
    plt.plot(list_lengths, bubble2_times, marker="o", label="bubblesort2 (shift)")
    plt.xlabel("List length (n)")
    plt.ylabel("Average time (seconds)")
    plt.title(f"Experiment 2: Bubble Sort vs bubblesort2")
    plt.legend()
    plt.tight_layout()
    plt.show()

    # Selection vs Selection2 (random)
    selection_times = []
    selection2_times = []
    for n in list_lengths:
        t1, t2 = avg_pair_times(bad.selection_sort, selectionsort2, n, runs, max_value, gen_select)
        selection_times.append(t1)
        selection2_times.append(t2)

    plt.figure()
    plt.plot(list_lengths, selection_times, marker="o", label="selection_sort (given)")
    plt.plot(list_lengths, selection2_times, marker="o", label="selectionsort2 (min+max)")
    plt.xlabel("List length (n)")
    plt.ylabel("Average time (seconds)")
    plt.title("Experiment 2: Selection Sort vs selectionsort2")
    plt.legend()
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    run_experiment2()
