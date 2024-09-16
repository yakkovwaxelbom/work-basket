def knapsack(items, limit):
    """
    Solves the 0/1 knapsack problem using dynamic programming.

    Args:
        items (list of tuples): Each tuple represents an item and contains three elements:
            - item: the item name (string)
            - weight: the weight of the item (int)
            - value: the value of the item (int)
        limit (int): The maximum weight capacity of the knapsack.

    Returns:
        list: A list of items that maximize the total value without exceeding the weight limit.

    Example:
        items = [
            ("item1", 2, 3),
            ("item2", 3, 4),
            ("item3", 4, 5),
            ("item4", 5, 6)
        ]
        limit = 5
        result = knapsack(items, limit)
        print(result)  # Output: [('item2', 3, 4), ('item1', 2, 3)]
    """
    table = [[0 for _ in range(limit + 1)] for _ in range(len(items) + 1)]

    for j in range(1, len(items) + 1):
        item, weight, value = items[j - 1]
        for w in range(1, limit + 1):
            if weight > w:
                table[j][w] = table[j - 1][w]
            else:
                table[j][w] = max(table[j - 1][w],
                                  table[j - 1][w - weight] + value)

    result = []
    w = limit
    for j in range(len(items), 0, -1):
        was_added = table[j][w] != table[j - 1][w]

        if was_added:
            item, wt, val = items[j - 1]
            result.append(items[j - 1])
            w -= wt

    return result


# Define the items as a list of tuples
items = [
    ("item1", 2, 3),
    ("item2", 3, 4),
    ("item3", 4, 5),
    ("item4", 5, 6)
]

# Define the weight limit of the knapsack
limit = 5

# Run the knapsack function
result = knapsack(items, limit)

# Print the result
print("Selected items:", result)
