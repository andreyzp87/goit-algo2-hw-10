import random
import time
import matplotlib.pyplot as plt


def deterministic_quick_sort(arr):
    if len(arr) <= 1:
        return arr

    pivot_idx = len(arr) // 2
    pivot = arr[pivot_idx]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return deterministic_quick_sort(left) + middle + deterministic_quick_sort(right)


def randomized_quick_sort(arr):
    if len(arr) < 2:
        return arr

    pivot_idx = random.randint(0, len(arr) - 1)
    pivot = arr[pivot_idx]

    left = []
    middle = []
    right = []

    for x in arr:
        if x < pivot:
            left.append(x)
        elif x == pivot:
            middle.append(x)
        else:
            right.append(x)

    return randomized_quick_sort(left) + middle + randomized_quick_sort(right)


def measure_sorting_time(sort_func, arr, iterations = 5):
    times = []
    for _ in range(iterations):
        arr_copy = arr.copy()
        start_time = time.time()
        sort_func(arr_copy)
        end_time = time.time()
        times.append(end_time - start_time)
    return sum(times) / len(times)


def create_comparison_plot(sizes, rand_times, det_times):
    plt.figure(figsize=(10, 6))
    plt.plot(sizes, rand_times, 'b-o', label='Рандомізований QuickSort')
    plt.plot(sizes, det_times, 'r-o', label='Детермінований QuickSort')
    plt.xlabel('Розмір масиву')
    plt.ylabel('Час виконання (секунди)')
    plt.title('Порівняння ефективності алгоритмів QuickSort')
    plt.legend()
    plt.grid(True)
    plt.savefig('quicksort_comparison.png')
    plt.show()

if __name__ == "__main__":
    sizes = [10_000, 50_000, 100_000, 500_000]
    randomized_times = []
    deterministic_times = []

    for size in sizes:
        arr = [random.randint(1, 1000_000) for _ in range(size)]

        rand_time = measure_sorting_time(randomized_quick_sort, arr)
        det_time = measure_sorting_time(deterministic_quick_sort, arr)

        randomized_times.append(rand_time)
        deterministic_times.append(det_time)

        print(f"Розмір масиву: {size}")
        print(f"   Рандомізований QuickSort: {rand_time:.4f} секунд")
        print(f"   Детермінований QuickSort: {det_time:.4f} секунд")

    create_comparison_plot(sizes, randomized_times, deterministic_times)

