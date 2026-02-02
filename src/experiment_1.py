import timeit
import matplotlib.pyplot as plt
from src.bad_sorts import bubble_sort, selection_sort, insertion_sort, create_random_list


# --- EXPERIMENT 1 --- 
# Compare runtimes of insertion, bubble and selection sort

def experiment1():
    # Experimental Parameters
    list_lengths = [10, 50, 100, 300, 500, 700, 1000] # List lengths (n)
    runs = 10  # Number of runs to average per data point
    
    # Storage for results
    results = {
        "Bubble Sort": [],
        "Selection Sort": [],
        "Insertion Sort": [],
    }

    print(f"Starting experiment1")

    for n in list_lengths:
        print(f"Testing length: {n}")
        
        # Define the tests
        tests = [
            ("Bubble Sort", lambda: bubble_sort(create_random_list(n, 1000))),
            ("Selection Sort", lambda: selection_sort(create_random_list(n, 1000))),
            ("Insertion Sort", lambda: insertion_sort(create_random_list(n, 1000))),
        ]

        for name, test_func in tests:
            # Time the execution
            time_taken = timeit.timeit(test_func, number=runs) / runs
            results[name].append(time_taken)

    # Plotting the Results
    plt.figure(figsize=(10, 6))
    
    for name, times in results.items():
        plt.plot(list_lengths, times, marker='o', label=name)

    plt.title("Bad Sorting Algorithm Performance")
    plt.xlabel("List Length (n)")
    plt.ylabel("Average Time (seconds)")
    plt.legend()
    plt.grid(True)
    plt.show()

if __name__ == "__main__":
    experiment1()
