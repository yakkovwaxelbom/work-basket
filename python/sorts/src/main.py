import random
import time
import matplotlib.pyplot as plt
from tqdm import tqdm
from sorts import SortUtils

# Test function to verify sorting algorithms
def test_sorting_algorithm(algorithms, n=10):
    for algo_func in algorithms.values():
        for _ in range(n):
            length = random.randint(10, 100)
            arr = [random.randint(100, 100_000) for _ in range(length)]
            expected = sorted(arr)
            assert algo_func(arr) == expected
        print(f"All test cases passed for {algo_func.__name__}")

# Function to plot the performance of sorting algorithms
def plot_sorting_performance(algorithms):
    lengths = [100, 500, 1_000, 5_000]
    for algo_name, algo_func in algorithms.items():
        execution_times = []
        for length in tqdm(lengths):
            arr = random.sample(range(length ** 3), length)
            start_time = time.time()
            algo_func(arr)
            end_time = time.time()
            execution_times.append(end_time - start_time)

        plt.plot(lengths, execution_times, label=algo_name)

    plt.xlabel("Array Length")
    plt.ylabel("Execution Time (seconds)")
    plt.legend()
    plt.show()

if __name__ == "__main__":
    algorithms = {
        'radix_sort': SortUtils.radix_sort,
        'quicksort': SortUtils.quicksort,
        'merge': SortUtils.merge_sort,
        'heapsort': SortUtils.heapsort,
        'insertion_sort': SortUtils.insertion_sort,
        'bubblesort': SortUtils.bubblesort,
        'counting_sort': SortUtils.counting_sort,
        'selection_sort': SortUtils.selection_sort
    }
    
    test_sorting_algorithm(algorithms)
    plot_sorting_performance(algorithms)
