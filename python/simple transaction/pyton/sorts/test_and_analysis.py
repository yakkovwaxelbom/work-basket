import time
import random
import matplotlib.pyplot as plt
from tqdm import tqdm

from sorts import SortUtils


#  Test function to verify sorting algorithms
def test_sorting_algorithm(algorithms, n=10):
    for algo_func in algorithms.values():
        # Perform n random test cases
        for _ in range(n):
            length = random.randint(10, 100)
            arr = [random.randint(100, 100_000) for _ in range(length)]
            expected = sorted(arr)
            # Verify that the sorted array matches the expected result
            assert algo_func(arr) == expected

        print("All test cases passed")


# Function to plot the performance of sorting algorithms
def plot_sorting_performance(algorithms):
    # Define the lengths of arrays for performance testing
    lengths = [100, 500, 1_000, 5_000]
    for algo_name, algo_func in algorithms.items():
        execution_times = []
        for length in tqdm(lengths):
            arr = random.sample(range(length ** 3), length)
            start_time = time.time()
            algo_func(arr)
            end_time = time.time()
            execution_times.append(end_time - start_time)

        # Plot the execution times for each array length
        plt.plot(lengths, execution_times, label=algo_name)

    plt.xlabel("Array Length")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.show()


algorithms = {
    'radix_sort': SortUtils.radix_sort, 'quicksort': SortUtils.quicksort, 'merge': SortUtils.merge_sort,
    'heapsort': SortUtils.heapsort, 'insertion_sort': SortUtils.insertion_sort,
    'bubblesort': SortUtils.bubblesort, 'counting_sort': SortUtils.counting_sort,
    'selection_sort': SortUtils.selection_sort
}

algorithms.values()
plot_sorting_performance(algorithms)
