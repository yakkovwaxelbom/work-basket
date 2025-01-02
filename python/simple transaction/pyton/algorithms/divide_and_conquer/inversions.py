def count_inversions_merge(a, start, mid, end):
    """
      Merges two sorted halves of the array and counts the number of inversions.

      Parameters:
      a (list): The array to be sorted and analyzed.
      start (int): The starting index of the first half.
      mid (int): The ending index of the first half and the starting index of the second half.
      end (int): The ending index of the second half.

      Returns:
      int: The number of inversions in the merged array.
      """
    positive_infinity = float('inf')
    size_right_side = mid - start
    size_left_side = end - mid
    right_side = [a[mid + i] for i in range(1, size_left_side + 1)]
    left_side = [a[start + i] for i in range(size_right_side + 1)]
    right_side.append(positive_infinity)
    left_side.append(positive_infinity)
    i, j = 0, 0
    count = 0  # Counting the permutations of the elements
    for k in range(start, end + 1):
        if left_side[i] <= right_side[j]:
            a[k] = left_side[i]
            i += 1
        else:
            count += len(left_side) - i - 1
            a[k] = right_side[j]
            j += 1
    # return a If we want a sorted array
    return count


def count_inversions_merge_sort(a, start, end, count):
    """
    Sorts the array using merge sort and counts the number of inversions.

    Parameters:
    a (list): The array to be sorted and analyzed.
    start (int): The starting index of the portion of the array to be sorted.
    end (int): The ending index of the portion of the array to be sorted.

    Returns:
    int: The total number of inversions in the array.
    """
    if start < end:  # I need to check what's going on here
        mid = ((end + start) // 2)
        left = count_inversions_merge_sort(a, start, mid, count)
        right = count_inversions_merge_sort(a, mid + 1, end, count)
        count = count_inversions_merge(a, start, mid, end) + left + right
    return count


def test_count_inversions_merge_sort():
    """
    Tests the count_inversions_merge_sort function with various test cases.
    """

    def run_test_case(array, expected_count):
        # Copy the array to avoid in-place modifications
        array_copy = array[:]
        count = count_inversions_merge_sort(array_copy, 0, len(array_copy) - 1)
        assert count == expected_count, f"Expected {expected_count}, got {count}"
        print(f"Test passed for array: {array_copy}")

    # Test cases
    run_test_case([3, 1, 2], 2)  # Test with a small array
    run_test_case([1, 2, 3], 0)  # Test with a sorted array
    run_test_case([2, 1, 3], 1)  # Test with a nearly sorted array
    run_test_case([5, 2, 6, 1], 4)  # Test with a larger array


if __name__ == "main":
    test_count_inversions_merge_sort()
