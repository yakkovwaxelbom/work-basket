import random
import sys

sys.path.append('/home/mefathim/PycharmProjects/מוגמר/data_structures')
print(sys.path)

from MinHeap import MinHeap


class SortUtils:
    @staticmethod
    def counting_sort(array):
        max_element = max(array)
        min_element = min(array)
        c = [0] * (max_element - min_element + 1)
        for i in range(len(array)):
            c[array[i] - min_element] += 1
        c[0] -= 1  # Because you start from 0
        for i in range(1, max_element - min_element + 1):
            c[i] += c[i - 1]
        b = [0] * len(array)
        for i in range(len(array) - 1, -1, -1):
            b[c[array[i] - min_element]] = array[i]
            c[array[i] - min_element] -= 1
        return b

    @staticmethod
    def heapsort(array):
        heap = MinHeap(array[:])
        for i in range(len(array)):
            array[i] = heap.extract_min()
        return array

    @staticmethod
    def bubblesort(array):
        for i in range(len(array)):
            for j in range(len(array) - 1, i, -1):
                if array[j] < array[j - 1]:
                    array[j], array[j - 1] = array[j - 1], array[j]
        return array

    @staticmethod
    def __merge(array, start, mid, end):
        size_right_side = mid - start
        size_left_side = end - mid

        right_side = [array[mid + i] for i in range(1, size_left_side + 1)]
        left_side = [array[start + i] for i in range(size_right_side + 1)]

        right_side.append(float('inf'))
        left_side.append(float('inf'))

        i, j = 0, 0

        for k in range(start, end + 1):
            if left_side[i] <= right_side[j]:
                array[k] = left_side[i]
                i += 1
            else:
                array[k] = right_side[j]
                j += 1

    @staticmethod
    def merge_sort(array, start, end):
        if start < end:
            mid = (end + start) // 2
            SortUtils.merge_sort(array, start, mid)
            SortUtils.merge_sort(array, mid + 1, end)
            SortUtils.__merge(array, start, mid, end)
        return array

    @staticmethod
    def __partition(array, start, end):
        axis_index = random.randrange(start, end)
        axis = array[axis_index]
        array[end], array[axis_index] = array[axis_index], array[end]
        pointer = start - 1
        for j in range(start, end):
            if array[j] <= axis:
                pointer += 1
                array[j], array[pointer] = array[pointer], array[j]
        array[pointer + 1], array[end] = array[end], array[pointer + 1]
        return pointer + 1

    @staticmethod
    def quicksort(array, start, end):
        if start < end:
            septal = SortUtils.__partition(array, start, end)
            SortUtils.quicksort(array, start, septal - 1)
            SortUtils.quicksort(array, septal + 1, end)
        return array

    @staticmethod
    def __conversion(a, func):
        str_numbers = list(map(func, a))
        return str_numbers

    @staticmethod
    def __padding(a):
        max_length = max(len(num) for num in a)
        padded_numbers = list(map(lambda x: x.zfill(max_length), a))
        return padded_numbers

    @staticmethod
    def __radix_counting_sort(array, base=10):
        count = [0] * base
        result = [''] * len(array)

        for d in range(len(array[0]) - 1, -1, -1):
            for i in range(len(array)):
                x = int(array[i][d], base)
                count[x] += 1

            for i in range(1, len(count)):
                count[i] += count[i - 1]

            for i in range(len(array) - 1, -1, -1):
                x = int(array[i][d], base)
                count_index = count[x] - 1
                result[count_index] = array[i]
                count[x] -= 1

            for i in range(len(array)):
                array[i] = result[i]
            count = [0] * base

        return array

    @staticmethod
    def radix_sort(array):
        array = SortUtils.__conversion(array, str)
        array = SortUtils.__padding(array)
        array = SortUtils.__radix_counting_sort(array)
        return SortUtils.__conversion(array, int)

    @staticmethod
    def selection_sort(array):
        for i in range(len(array) - 1):
            min_index = i
            for j in range(i + 1, len(array)):
                if array[j] < array[min_index]:
                    min_index = j
            array[i], array[min_index] = array[min_index], array[i]
        return array

    @staticmethod
    def insertion_sort(arr):
        for i in range(1, len(arr)):
            j = i
            while arr[j - 1] > arr[j] and j > 0:
                arr[j - 1], arr[j] = arr[j], arr[j - 1]
                j -= 1
        return arr


print(SortUtils.heapsort([2, 1, 4]))
