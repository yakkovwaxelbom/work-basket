import threading
import random
import math
import queue
from tqdm import tqdm

NUM_POINTS = 10 ** 6

points_queue = queue.Queue()
lock = threading.Lock()
inside_circle_count = 0


def generate_points(num_points, points_queue):
    """ Generate random points and add them to the queue """
    for _ in tqdm(range(num_points)):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)
        points_queue.put((x, y))
    points_queue.put(None)  # Signal the consumer to stop


def check_points(points_queue):
    """ Check if points are inside the circle """
    global inside_circle_count

    while True:
        point = points_queue.get(block=True)
        if point is None:  # Stop signal
            return
        x, y = point
        if math.sqrt(x ** 2 + y ** 2) <= 1:
            with lock:
                inside_circle_count += 1


def monte_carlo_pi(num_points):
    """ Calculate the approximation of π using Monte Carlo """
    producer_thread = threading.Thread(target=generate_points, args=(num_points, points_queue))
    consumer_thread = threading.Thread(target=check_points, args=(points_queue,))

    producer_thread.start()
    consumer_thread.start()

    producer_thread.join()
    consumer_thread.join()

    pi_estimate = 4 * inside_circle_count / num_points
    return pi_estimate


if __name__ == "__main__":
    pi_approximation = monte_carlo_pi(NUM_POINTS)
    print(f"Approximation of π using {NUM_POINTS} points: {pi_approximation}")
