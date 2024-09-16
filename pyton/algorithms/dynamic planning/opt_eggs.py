"""
Egg Dropping Problem - Dynamic Programming Solution

### Background:
The egg dropping problem is a classic example of dynamic programming that explores the minimum number of attempts
 required to determine from which floor an egg can be dropped without breaking. 
The problem can be summarized as follows:

You are given `N` floors and `E` eggs. You need to determine the critical floor, the highest floor from which you can
 drop an egg such that it doesn't break. The challenge is to minimize the number of drops (tests) in the worst-case
  scenario.

Key constraints:
- If an egg breaks when dropped from floor `t`, it will break from any floor higher than `t`.
- If an egg doesn't break when dropped from floor `t`, it will not break from any floor lower than `t`.

### Goal:
The code calculates the minimum number of attempts required to find this critical floor in the worst-case scenario,
 using dynamic programming. The formula for solving the larger problem recursively is:
Where:
- `n` is the number of floors.
- `e` is the number of eggs.
- The idea is to try dropping an egg from every possible floor and calculate the worst-case outcome 
(either the egg breaks or it doesn’t).

### Time Complexity:
The time complexity of the solution is **O(N*E)** where:
- `N` is the number of floors.
- `K` is the number of eggs.

This is because for each egg, we evaluate every floor and compute the result based on previous results stored in
 a table.

### Parameters:
- `floors (int)`: The number of floors in the building (N).
- `eggs (int)`: The number of eggs available for the problem (E).

Functions:
    1. table_opt(floors, eggs) -> list[list[int]]:
        - Initializes a dynamic programming table `table` with `eggs + 1` rows and `floors + 1` columns.
        - The first row and column are set based on the base cases (1 egg and 1 floor scenarios).

    2. compute_opt(floors, eggs, table) -> int:
        - Fills the dynamic programming table based on the recurrence relation. 
        - The result at `table[eggs][floors]` represents the minimum number of attempts needed in the worst case.

    3. manager_opt(floors, eggs) -> int:
        - Manages the setup and solution computation by initializing the table and calling the solver.

Returns:
    - The minimum number of attempts required in the worst-case scenario to find the critical floor.

Example:
    manager_opt(100, 2) -> 14
    This represents the minimum number of attempts required with 2 eggs and 100 floors.

"""
import math


def table_opt(floors, eggs) -> any:
    table = [[0 for _ in range(floors + 1)] for _ in range(eggs + 1)]
    for i in range(floors + 1):
        table[1][i] = i
    for i in range(1, eggs + 1):
        table[i][1] = 1
    return table


# Solve larger problems according to the formula f(n,e) = 1+min(1<=t<=n)max((t,e-1),(n-t,e)
def compute_opt(floors, eggs, table) -> int:
    for egg in range(2, eggs + 1):
        for floor in range(2, floors + 1):
            list_of_current_max = []
            for j in range(1, floor + 1):
                list_of_current_max.append(max(table[egg - 1][j - 1], table[egg][floor - j]))
            table[egg][floor] = 1 + min(list_of_current_max)
    return table[eggs][floors]


def manager_opt(floors, eggs) -> int:
    table = table_opt(floors, eggs)
    return compute_opt(floors, eggs, table)


"""
two_eggs_by_finding_series(floor) -> int:
    Egg Dropping Problem with Two Eggs

### Problem Description:
This function solves a specific case of the egg dropping problem where we have exactly **two eggs** and we want to 
determine the minimum number of attempts required to find the critical floor
 (the highest floor from which an egg can be dropped without breaking) in a building with `floor` floors.

Key Constraints:
- We have **two eggs**.
- We want to minimize the number of attempts in the worst-case scenario.

### Approach:
The strategy for solving this problem with two eggs involves progressively increasing the number of floors from which we
 drop the first egg. 
- Initially, the first egg is dropped from floor `1`, then from a higher floor (`x+1`), increasing the drop height until
 we find the critical floor.
- If the first egg breaks, we use the second egg to perform a linear search from the last safe floor up to the critical 
floor.

This function determines the number of attempts needed in the worst case to solve the problem based on the input number
 of floors (`floor`).

### Array Representation:
If we represent the number of attempts in an array where:
- The first element represents the solution for 2 eggs and 1 floor,
- The second element represents the solution for 2 eggs and 2 floors,
- And so on...

The resulting array would look like:
This means:
- For 1 floor, 1 drop is needed.
- For 2 floors, 2 drops are needed.
- For 3 floors, 2 drops are still sufficient.
- For 4 floors, 3 drops are required, and so on.

### Parameters:
- `floor (int)`: The number of floors in the building.

### Returns:
- `int`: The minimum number of attempts needed in the worst case with 2 eggs and `floor` floors.

### Example:
    two_eggs_by_finding_series(10) -> 4
    This means with 10 floors and 2 eggs, you need 4 drops in the worst-case scenario.

"""


def two_eggs_by_finding_series(floor) -> int:
    if floor == 1:
        return 1
    x = 1
    count = 1
    while x < floor:
        x += count + 1
        count += 1
    return count


"""
two_eggs_by_Analysis(floor) -> float:
    Egg Dropping Problem with Two Eggs (Using Arithmetic Progression)

### Problem Description:
This function solves the egg dropping problem with **two eggs** by leveraging the formula for an arithmetic progression
 (AP). The problem is to find the minimum number of drops (`x`) such that the total number of floors checked is at least
  equal to the given number of floors (`floor`).

### Approach:
The arithmetic progression (AP) is structured such that:
- The first term (`a`) is the number of eggs you need to drop at each step, which is `x`.
- The last term of the progression is `1`, meaning that by the time you've reached the last drop, only one floor is
 left to check.

The sum of this arithmetic progression needs to be **greater than or equal to** the total number of floors. This sum is
 calculated as:

Solving this equation for `x` (the number of drops), we arrive at a quadratic equation:

The function solves this quadratic equation using the quadratic formula:
Where:
- `a = 1` (coefficient of `x^2`),
- `b = 1` (coefficient of `x`),
- `c = -2 * floor` (constant term).

The solution gives us the smallest integer value `x` that satisfies the inequality.

### Parameters:
- `floor (int)`: The number of floors in the building.

### Returns:
- `float`: The minimum number of drops needed to check all floors, rounded up to the nearest integer.

### Example:
    two_eggs1(10) -> 4
    This means with 10 floors and 2 eggs, the minimum number of drops needed is 4.

### Key Points:
- This solution is derived from an **arithmetic progression** where:
  - The first term is `x` (the number of eggs to drop at each step).
  - The last term is `1` (since the progression decreases until we have only one floor left).
- The sum of the series must be **greater than or equal to** the number of floors (`floor`), and this is solved using
 the quadratic formula.
"""


def two_eggs_by_Analysis(floor) -> float:
    a = 1
    b = 1
    c = -2 * floor
    return math.ceil((-b + (b ** 2 - 4 * a * c) ** 0.5) / (2 * a))
