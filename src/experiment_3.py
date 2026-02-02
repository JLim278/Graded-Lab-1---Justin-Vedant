import timeit
import matplotlib.pyplot as plt
from src.bad_sorts import bubble_sort, selection_sort, insertion_sort, create_near_sorted_list


#--- EXPERIMENT 3 ---
def experiment3():
    # Parameters
    length = 5000 
    swap_values = [0, 100, 500, 1000, 5000, 10000, 20000, 30000]
    runs = 10
    
    results = {"Bubble Sort": [], "Selection Sort": [], "Insertion Sort": []}

    print(f"Running Experiment 3 (n={length})...")

    for s in swap_values:
        print(f"Testing swaps: {s}")
        
        test_bubble = lambda: bubble_sort(create_near_sorted_list(length, 1000, s))
        test_selection = lambda: selection_sort(create_near_sorted_list(length, 1000, s))
        test_insertion = lambda: insertion_sort(create_near_sorted_list(length, 1000, s))

        results["Bubble Sort"].append(timeit.timeit(test_bubble, number=runs) / runs)
        results["Selection Sort"].append(timeit.timeit(test_selection, number=runs) / runs)
        results["Insertion Sort"].append(timeit.timeit(test_insertion, number=runs) / runs)

    # Plotting
    plt.figure(figsize=(10, 6))
    for name, times in results.items():
        plt.plot(list(swap_values), times, marker='o', label=name)

    plt.title(f"Impact of Sortedness on Performance")
    plt.xlabel("Number of Swaps")
    plt.ylabel("Average Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()


if __name__ == "__main__":
    experiment3()