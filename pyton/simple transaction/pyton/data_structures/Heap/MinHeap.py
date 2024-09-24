class MinHeap:
    def __init__(self, array: list):
        self.__array = array
        self.__size = len(array)  # self.size = len(array)
        self.__build_min_heap()

    def increase_value(self, i, value):
        parent = self.__parent(i)
        if value < self.__array[i]:
            return "error"
        self.__array[i] = value
        while i > 1 and self.__array[parent] > self.__array[i]:
            self.__array[i], self.__array[parent] = self.__array[parent], self.__array[i]
            i = parent

    def heap_insert(self, value):
        positive_infinity = float('inf')
        self.__size += 1
        self.__array.append(positive_infinity)
        self.increase_value(self.__size, value)

    def extract_min(self):
        if not self.__is_empty():
            get_min = self.__array[0]
            self.__array[0] = self.__array[self.__size - 1]
            del self.__array[self.__size - 1]
            self.__size -= 1
            self.min_heapify(0)
            return get_min

    def get_min(self):
        return self.__array[0]

    def min_heapify(self, index):
        left = self.__left(index)
        right = self.__right(index)
        smallest = index
        if left and self.__array[left] < self.__array[smallest]:
            smallest = left
        if right and self.__array[right] < self.__array[smallest]:
            smallest = right
        if smallest != index:
            self.__array[index], self.__array[smallest] = self.__array[smallest], self.__array[index]
            self.min_heapify(smallest)

    def __build_min_heap(self):
        for j in range(self.size // 2 - 1, -1, -1):
            self.min_heapify(j)

    def __is_empty(self):
        return self.__size == 0

    @property
    def size(self):
        return self.__size

    def __left(self, i):
        left = 2 * i + 1
        return left if left < self.__size else None

    def __right(self, i):
        right = 2 * i + 2
        return right if right < self.__size else None

    def __parent(self, i):
        if i < self.__size:
            return (i - 1) // 2

    def __str__(self):
        return str(self.__array)

    def __len__(self):
        return self.__size

    def __lt__(self, other):
        return self.__size < len(other)

    def __le__(self, other):
        return self.__size <= len(other)

    def __gt__(self, other):
        return self.__size > len(other)

    def __ge__(self, other):
        return self.__size >= len(other)
