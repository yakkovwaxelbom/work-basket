class LinkedList:
    class Node:

        def __init__(self, data=None, next=None):
            self.__data = data
            self.__next = next

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, value):
            self.__data = value

        @property
        def next(self):
            return self.__next

        @next.setter
        def next(self, next_node):
            self.__next = next_node

        def __str__(self):
            return str(self.__data)

        def __eq__(self, other):
            if not isinstance(other, LinkedList.Node):
                return NotImplemented
            return self.__data == other.__data

        def __lt__(self, other):
            if not isinstance(other, LinkedList.Node):
                return NotImplemented
            return self.__data < other.__data

        def __le__(self, other):
            if not isinstance(other, LinkedList.Node):
                return NotImplemented
            return self.__data <= other.__data

        def __gt__(self, other):
            if not isinstance(other, LinkedList.Node):
                return NotImplemented
            return self.__data > other.__data

        def __ge__(self, other):
            if not isinstance(other, LinkedList.Node):
                return NotImplemented
            return self.__data >= other.__data

        def __hash__(self):
            return hash(self.__data)

        def __repr__(self):
            return f"Node(data={self.__data}, next={self.__next})"

    """A class representing a singly linked list."""

    def __init__(self):
        self.__head = None
        self.__tail = None

    def add(self, n):
        """Adds a new node with the given value to the end of the list.

        Args:
            n (Any): The value to be added.
        """
        new_node = LinkedList.Node(n)
        if not self.__head:
            self.__head = new_node
            self.__tail = new_node
        else:
            self.__tail.next = new_node
            self.__tail = new_node

    def remove(self, n):
        """Removes the first node with the given value from the list.

        Args:
            n (Any): The value to be removed.
        """
        if not self.__head:
            return

        # Special case: removing the head node
        if self.__head.get_data() == n:
            self.__head = self.__head.get_next()
            return

        current = self.__head
        while current.get_next() and current.get_next().get_data() != n:
            current = current.get_next()

        if current.get_next():
            current.set_next(current.get_next().get_next())

    @property
    def head(self):
        return self.__head

    def set_head(self, n):
        """Sets a new node as the head of the list.

        Args:
            n (Any): The value for the new head node.
        """
        new_head = LinkedList.Node(n)
        new_head.next = self.__head
        self.__head = new_head

    def search(self, value):
        """Searches for a value in the list and returns True if found, otherwise False.

        Args:
            value (Any): The value to search for.

        Returns:
            bool: True if the value is found, otherwise False.
        """
        current = self.__head
        while current:
            if current.get_data() == value:
                return True
            current = current.get_next()
        return False

    def is_empty(self):
        """Checks if the list is empty.

        Returns:
            bool: True if the list is empty, otherwise False.
        """
        return self.__head is None

    def __str__(self):
        """Returns a string representation of the linked list.

        Returns:
            str: A string representation of the list.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.get_data()) + " --> "
            current = current.get_next()
        result += 'None'
        return result

    def __iter__(self):
        """Returns an iterator for the linked list."""
        current = self.__head
        while current:
            yield current.get_data()
            current = current.get_next()
