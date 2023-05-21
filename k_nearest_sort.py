import matplotlib.pyplot as plt

import random  # to add randomness to the arrays being created
import time  # to compare the algorithms' running times

id = 201742  # seed of the elements of the array (totally random)
size = [10 ** 2, 10 ** 3, 10 ** 4]  # given sizes
# size = [5, 10] # can be tried with much more quick respectively

orgin_arr = []  # to keep the original array

time_arr_quick_sort = []  # the sorting times by quick sort
time_arr_heap_sort = []  # the sorting times by heap sort

arr_sorted_quick = []  # the array sorted by heap sort
arr_sorted_heap = []  # the array sorted by heap sort


def main():  # in order to start the program
    flow()


def flow():  # in order to provide the program flow
    global arr_sorted_quick, arr_sorted_heap
    global orgin_arr
    for i in size:
        arr, k = generate_arr(i)

        end_time_quick_sort = time.time()
        quick_sort(arr, 0, k - 1)
        arr_sorted_quick = arr.copy()
        time_arr_quick_sort.append(end_time_quick_sort)
        print_res(arr_sorted_quick, k, end_time_quick_sort)
        control(arr_sorted_quick)

        arr = (orgin_arr.copy())  # arr is changed (sorted) in quicksort and so, here it is re-assigned as the original one which also is sent to quick_sort()
        end_time_heap_sort = time.time()
        arr_sorted_heap = min_heap_sort(arr, k + 1)
        time_arr_heap_sort.append(end_time_heap_sort)
        print_res(arr, k, end_time_heap_sort)
        control(arr_sorted_heap)
        print("*********************************************", "\n")

    plot_time()


def generate_arr(i):  # in order to create random arrays and the "k" values dependently on the array sizes being creted
    global orgin_arr
    arr = []

    for j in range(i):
        curr_rand = int(random.random() * id)
        if curr_rand not in arr:
            arr.append(int(random.random() * id))

        orgin_arr = arr.copy()

    k = int(random.randint(1, len(arr) - 1))

    return arr, k


def partition(arr, low, high):
    i = low - 1
    pivot = arr[high]

    for j in range(low, high):
        if arr[j] <= pivot:
            i = i + 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[i + 1], arr[high] = arr[high], arr[i + 1]
    return i + 1


def quick_sort(arr, low, high):
    if len(arr) == 1:
        return arr
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)
        quick_sort(arr, pi + 1, high)


def heapify(arr, n, i):
    smallest = i

    l = 2 * i + 1
    r = 2 * i + 2

    if l < n and arr[l] < arr[smallest]:
        smallest = l

    if r < n and arr[r] < arr[smallest]:
        smallest = r

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        heapify(arr, n, smallest)


def min_heap_sort(arr, n):
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(arr, n, i)

    for i in range(n - 1, -1, -1):
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)

    return arr


def print_res(arr, n, end_time):  # in order to print the results in a structured way
    print(
        "orginal array created randomly \n",
        orgin_arr,
        "\n\n\n",
        "sorted array with randomly chosen k = ",
        n,
        "\n",
        arr,
        "\n\n with runtime: ",
        end_time,
    )


def plot_time():  # in order to visualize the running times
    plt.title("Run Times Comparison")
    plt.xlabel("array sizes sorted")
    plt.ylabel("run times in millis")
    plt.plot(size, time_arr_quick_sort, color="g", label="Quick Sort")
    plt.plot(size, time_arr_heap_sort, color="r", label="Heap Sort")

    plt.show()


def control(arr):
    distances = []
    for curr_elem in orgin_arr:
        orgin_position = orgin_arr.index(curr_elem)
        sorted_position = arr.index(curr_elem)
        distances.append(abs(orgin_position - sorted_position))

    max_distance = max(distances)
    print("max distance between the elements sorted and unsorted is = ", max_distance)


if __name__ == "__main__":
    main()
