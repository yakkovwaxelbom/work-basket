import os
import cv2
from PIL import Image
import numpy as np
from containers import Matrix2D, SetMinHeap, Node


class MazeSolver:
    @staticmethod
    def __load_and_process_image(image_input):
        format_type = MazeSolver.__is_valid_format(image_input)
        cv2_image = MazeSolver.__conversion_to_cv2(image_input, format_type)
        if cv2_image is None:
            raise Exception("input error")
        img_one_less_dim = cv2_image.min(2)
        return Matrix2D(img_one_less_dim > 200)

    @staticmethod
    def __is_valid_format(image_input):
        if isinstance(image_input, str):
            if os.path.isfile(image_input) and image_input.lower().endswith(('.png', '.jpg', '.jpeg')):
                return str
        elif isinstance(image_input, Image.Image):
            return Image.Image
        elif isinstance(image_input, np.ndarray):
            return np.ndarray
        return None

    @staticmethod
    def __conversion_to_cv2(image_input, input_type):
        conversion_functions = {
            str: lambda x: cv2.imread(x, cv2.IMREAD_COLOR) if os.path.isfile(x) else None,
            Image.Image: lambda x: cv2.cvtColor(np.array(x), cv2.COLOR_RGB2BGR),
            np.ndarray: lambda x: x
        }
        conversion_function = conversion_functions.get(input_type)

        if conversion_function:
            return conversion_function(image_input)
        else:
            return None

    @staticmethod
    def __analyze_by_dijkstra(boolean_graph, pos_start, pos_end):
        if min(*pos_start, *pos_end) < 0 and max(*pos_start, *pos_end) > len(boolean_graph[0]):
            raise ValueError("Start or end point must be valid")

        # Initialize the heap with the start node
        heap = SetMinHeap([Node(position=pos_start, distance=0)])
        heap.insert(Node(position=pos_end))  # Add the end node

        # Set to track visited nodes
        seen = set()

        # Perform Dijkstra's algorithm
        while pos_end not in seen:
            if heap.size == 0:
                raise ValueError("No path found")

            current_min = heap.extract_min()
            pos_x, pos_y = current_min.position
            seen.add((pos_x, pos_y))

            # Define the neighbors' positions
            neighbors = [(pos_x + 1, pos_y), (pos_x - 1, pos_y), (pos_x, pos_y + 1), (pos_x, pos_y - 1)]

            for nx, ny in neighbors:
                if min(nx, ny) >= 0 and max(nx, ny) <= len(boolean_graph[0]) - 1 and boolean_graph[(nx, ny)]:
                    if (nx, ny) not in heap:
                        heap.insert(
                            Node(position=(nx, ny), parent=current_min.position, distance=current_min.distance + 1)
                        )
                    else:
                        neighbor = heap[(nx, ny)]
                        if current_min.distance + 1 < neighbor.distance:
                            neighbor.parent = current_min.position
                            neighbor.distance = current_min.distance + 1

        return MazeSolver.__extract_path(heap, pos_end)

    @staticmethod
    def __extract_path(nodes: SetMinHeap, pos_end):
        path = []
        current = nodes[pos_end]
        while current.parent is not None:
            path.append(current.position)
            current = nodes[current.parent]
        return path

    @staticmethod
    def solv(image_input, pos_start, pos_end):
        boolean_graph = MazeSolver.__load_and_process_image(image_input)
        return MazeSolver.__analyze_by_dijkstra(boolean_graph, pos_start, pos_end)
