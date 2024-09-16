from typing import Optional, List, Union, Any, Tuple
from dataclasses import dataclass, field


class Matrix2D:
    def __init__(self, matrix: List[List[bool]]):
        self.__matrix = matrix

    def __getitem__(self, item: Tuple[int, int] | int) -> Union[Any, List[Any]]:
        if isinstance(item, tuple):
            row, col = item
            if row >= len(self.__matrix) or col >= len(self.__matrix[0]):
                raise IndexError("Index out of range")
            return self.__matrix[row][col]
        elif isinstance(item, int):
            if item >= len(self.__matrix):
                raise IndexError("Row index out of range")
            return self.__matrix[item]  # Return the whole row
        else:
            raise TypeError("Index must be an integer or a tuple of two integers")


@dataclass(order=True)
class Node:
    position: tuple[int, int] = field(compare=False)
    parent: Optional['tuple[int, int]'] = field(default=None, compare=False)
    distance: float = field(default=float('inf'))


class SetMinHeap:
    @dataclass(order=True)
    class HeapItem:
        value: Node
        index: int = field(compare=False)

    def __init__(self, nodes: Optional[list[Node]] = None):
        self.__dec = {}
        self.__heap = []
        self.__size = 0
        # It can be optimized at runtime O(n) but it is important here
        if nodes is not None:
            for node in nodes:
                self.insert(node)

    def insert(self, value):
        data = SetMinHeap.HeapItem(value=value, index=self.__size)
        self.__heap.append(data)
        self.__dec[value.position] = data
        self.__fix_up(self.__size)
        self.__size += 1

    @property
    def dec(self):
        return self.__dec

    @property
    def size(self):
        return self.__size

    def __fix_up(self, index: int):
        while index > 0:
            parent = self.__parent(index)
            if parent is not None and self.__heap[index] < self.__heap[parent]:
                self.__heap[index], self.__heap[parent] = self.__heap[parent], self.__heap[index]
                self.__heap[index].index, self.__heap[parent].index = parent, index
                index = parent
            else:
                break

    def __fix_down(self, index):
        while True:
            left = self.__left(index)
            right = self.__right(index)
            smallest = index

            if left is not None and self.__heap[left] < self.__heap[smallest]:
                smallest = left

            if right is not None and self.__heap[right] < self.__heap[smallest]:
                smallest = right

            if smallest != index:
                self.__heap[index], self.__heap[smallest] = self.__heap[smallest], self.__heap[index]
                self.__heap[index].index, self.__heap[smallest].index = self.__heap[smallest].index, index
                index = smallest
            else:
                break

    def extract_min(self) -> Node:
        if self.__size == 0:
            raise IndexError("Heap is empty")
        min_item, self.__heap[0] = self.__heap[0], self.__heap.pop()
        self.__size -= 1
        self.__heap[0].index = 0
        self.__fix_down(0)
        return min_item.value

    def increase_dis(self, i, value):
        if i >= self.__size:
            raise IndexError("Index out of range")

        old_value, self.__heap[i].value.distance = self.__heap[i].value.distance, value

        if value < old_value:
            self.__fix_up(i)
        else:
            self.__fix_down(i)

    def __contains__(self, position: Tuple[int, int]) -> bool:
        return position in self.__dec

    def __getitem__(self, pos: Tuple[int, int]) -> Node:
        return self.__dec[pos].value

    def __str__(self) -> str:
        return f"Heap: {[item.value.distance for item in self.__heap]}, Size: {self.__size}"

    def __left(self, i):
        left = 2 * i + 1
        return left if left < self.__size else None

    def __right(self, i):
        right = 2 * i + 2
        return right if right < self.__size else None

    def __parent(self, i):
        if i <= self.__size:
            return (i - 1) // 2
