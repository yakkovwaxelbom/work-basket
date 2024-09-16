import random
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D  # Required for 3D plots


def get_coordinates_system(dimensions, num_of_steps):
    """
    Initialize the coordinates system with zeros.

    Args:
    - dimensions (int): The number of dimensions in the system.
    - num_of_steps (int): The number of steps in the walk.

    Returns:
    - list of lists: A 2D list representing the coordinates system.
    """
    return [[0 for _ in range(num_of_steps + 1)] for _ in range(dimensions)]


def take_a_step(coordinates_system, step_dimension, step_num):
    """
    Take a step in a random direction in a given dimension.

    Args:
    - coordinates_system (list of lists): The coordinates system.
    - step_dimension (int): The dimension in which to take a step.
    - step_num (int): The current step number.
    """
    random_direction = random.sample([-1, 1], 1)[0]
    coordinates_system[step_dimension][step_num] = (
            coordinates_system[step_dimension][step_num - 1] + random_direction)


def stay_put_in_all_other_dimensions(coordinates_system, step_dimension, step_num):
    """
    Stay in the same position in all dimensions except the one specified.

    Args:
    - coordinates_system (list of lists): The coordinates system.
    - step_dimension (int): The dimension in which to move.
    - step_num (int): The current step number.
    """
    for dimension in range(len(coordinates_system)):
        if dimension != step_dimension:
            coordinates_system[dimension][step_num] = coordinates_system[dimension][step_num - 1]


def walk(coordinates_system, dimensions, num_of_steps):
    """
    Perform a random walk in the specified dimensions and number of steps.

    Args:
    - coordinates_system (list of lists): The coordinates system.
    - dimensions (int): The number of dimensions.
    - num_of_steps (int): The number of steps in the walk.
    """
    for step in range(1, num_of_steps + 1):
        random_dimension = random.randint(0, dimensions - 1)
        take_a_step(coordinates_system, random_dimension, step)
        stay_put_in_all_other_dimensions(coordinates_system, random_dimension, step)


def display_data(coordinates_system, dimensions, num_of_steps):
    """
    Display the random walk data.

    Args:
    - coordinates_system (list of lists): The coordinates system.
    - dimensions (int): The number of dimensions.
    - num_of_steps (int): The number of steps in the walk.
    """
    if dimensions == 1:
        plt.plot([step for step in range(num_of_steps + 1)], coordinates_system[0])
    elif dimensions == 2:
        plt.plot(coordinates_system[0], coordinates_system[1])
    else:
        fig = plt.figure()
        axes = fig.add_subplot(111, projection="3d")
        axes.plot(coordinates_system[0], coordinates_system[1], coordinates_system[2])
    plt.show()


def random_walk(dimensions, num_of_steps):
    """
    Perform a random walk in the specified dimensions and number of steps, and display the results.

    Args:
    - dimensions (int): The number of dimensions.
    - num_of_steps (int): The number of steps in the walk.
    """
    coordinates_system = get_coordinates_system(dimensions, num_of_steps)
    walk(coordinates_system, dimensions, num_of_steps)
    display_data(coordinates_system, dimensions, num_of_steps)


if __name__ == '__main__':
    # Main program
    dimensions = int(input("Please enter the number of dimensions you would like to roam: "))
    while not 1 <= dimensions <= 3:
        dimensions = int(input("Invalid input! Please enter a number between 1 and 3: "))
    print("Great!")

    num_of_steps = int(input("Please enter the number of steps you would like to walk: "))
    while num_of_steps <= 0:
        num_of_steps = int(input("Invalid input! Please enter a positive integer for the number of steps: "))
    print("Great!")

    random_walk(dimensions, num_of_steps)
