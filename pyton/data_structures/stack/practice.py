import random

from stack import Stack


def insert_min(s: Stack, n: int) -> None:
    """Insert the minimum element at the bottom of the stack while sorting.

    Args:
        s (Stack): The stack to be sorted.
        n (int): The number of elements to consider for sorting in the stack.

    Notes:
        This function is used to recursively sort the stack by inserting the minimum element at the bottom.
        It does not use any auxiliary data structures.

    Explanation:
        - The function pops two elements from the stack, finds the minimum and maximum, and pushes the minimum
          back to the stack.
        - It then recursively calls itself to sort the remaining elements.
        - Finally, it pushes the maximum element back to the stack after sorting the rest.
    """
    if n >= 2:
        a = s.pop()
        b = s.pop()
        s.push(min(a, b))
        insert_min(s, n - 1)
        s.push(max(a, b))


def sort_stack(s: Stack, n: int) -> None:
    """Sort the stack using recursive approach without additional data structures.

    Args:
        s (Stack): The stack to be sorted.
        n (int): The number of elements to consider for sorting in the stack.

    Notes:
        This function sorts the stack by recursively calling `insert_min` to place the minimum elements in order.
        It does not use any auxiliary data structures.

    Explanation:
        - The function calls `insert_min` to place the smallest element at the bottom of the stack.
        - It then recursively sorts the remaining elements in the stack.
    """
    if n >= 1:
        insert_min(s, n)
        sort_stack(s, n - 1)


def generate_random_stack_and_arr(size, min_value, max_value):
    stack = Stack()
    arr = []
    for _ in range(size):
        num = random.randint(min_value, max_value)
        arr.append(num)
        stack.push(num)
    return stack, arr


def test_sort_stack(num_tests=100, stack_size=100, min_value=-1000, max_value=1000):
    for _ in range(num_tests):
        stack, arr = generate_random_stack_and_arr(stack_size, min_value, max_value)
        arr.sort()
        sort_stack(stack, stack.size())
        assert arr == stack.stack, f"Test failed! Expected: {arr}, but got: {stack.stack}"


def check_properly_nested(string: str) -> bool:
    """Check if the parentheses, braces, and brackets in the string are properly nested.

    Args:
        string (str): The string containing the characters to be checked.

    Returns:
        bool: True if the string is properly nested, False otherwise.
    """
    if len(string) == 0:
        return True

    stack = Stack()
    matching_brackets = {')': '(', ']': '[', '}': '{'}

    for char in string:
        if char in matching_brackets.values():  # If it's one of '(', '{', '['
            stack.push(char)
        elif char in matching_brackets:  # If it's one of ')', ']', '}'
            if stack.is_empty():
                return False
            top = stack.pop()
            if top != matching_brackets[char]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    test_sort_stack()
