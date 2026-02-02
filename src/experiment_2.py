import timeit
import matplotlib.pyplot as plt
from src.bad_sorts import bubble_sort, selection_sort, create_random_list, create_near_sorted_list

# Experiment 2: bubble variation
# Shift based bubble
def bubblesort2(L):
    n = len(L)
    for end in range(n - 1, 0, -1):
        j = 0
        while j < end:
            if L[j] <= L[j + 1]:
                j += 1
            else:
                value = L[j]
                k = j
                while k < end and value > L[k + 1]:
                    L[k] = L[k + 1]
                    k += 1
                L[k] = value
                j = k


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

        L[left], L[min_i] = L[min_i], L[left]

        if max_i == left:
            max_i = min_i

        L[right], L[max_i] = L[max_i], L[right]
        left += 1
        right -= 1



def avg_pair_times(sort_a, sort_b, n, runs, max_value, near=False):
    total_a = 0.0
    total_b = 0.0

    for _ in range(runs):
        if near:
            base = create_near_sorted_list(n, max_value, 10)
        else:
            base = create_random_list(n, max_value)

        A = base.copy()
        start = timeit.default_timer()
        sort_a(A)
        total_a += timeit.default_timer() - start

        B = base.copy()
        start = timeit.default_timer()
        sort_b(B)
        total_b += timeit.default_timer() - start

    return total_a / runs, total_b / runs



# plotting (2 graphs)
def run_experiment2():

    list_lengths = [200, 400, 600, 800, 1000, 1200, 1400, 1600, 1800, 2000]
    runs = 5
    max_value = 10**6

    # Bubble (near sorted) 
    bubble_times = []
    bubble2_times = []

    for n in list_lengths:
        t1, t2 = avg_pair_times(bubble_sort, bubblesort2, n, runs, max_value, near=True)
        bubble_times.append(t1)
        bubble2_times.append(t2)

    plt.figure(figsize=(10, 6))
    plt.plot(list_lengths, bubble_times, marker='o', label="bubble_sort")
    plt.plot(list_lengths, bubble2_times, marker='o', label="bubblesort2")
    plt.title("Experiment 2: Bubble Sort vs bubblesort2")
    plt.xlabel("List Length (n)")
    plt.ylabel("Average Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

    # Selection (random)
    selection_times = []
    selection2_times = []

    for n in list_lengths:
        t1, t2 = avg_pair_times(selection_sort, selectionsort2, n, runs, max_value)
        selection_times.append(t1)
        selection2_times.append(t2)

    plt.figure(figsize=(10, 6))
    plt.plot(list_lengths, selection_times, marker='o', label="selection_sort")
    plt.plot(list_lengths, selection2_times, marker='o', label="selectionsort2")
    plt.title("Experiment 2: Selection Sort vs selectionsort2")
    plt.xlabel("List Length (n)")
    plt.ylabel("Average Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()



if __name__ == "__main__":
    run_experiment2()
