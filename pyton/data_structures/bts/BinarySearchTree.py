class BinarySearchTree:
    class TreeNode:
        def __init__(self, value=None):
            self.__data = value
            self.__right = None
            self.__left = None
            self._parent = None

        @property
        def data(self):
            return self.__data

        @data.setter
        def data(self, data):
            self.__data = data

        @property
        def left(self):
            return self.__left

        @left.setter
        def left(self, node):
            self.__left = node

        @property
        def right(self):
            return self.__right

        @right.setter
        def right(self, node):
            self.__right = node

        def __str__(self):
            return str(self.__data)

        def __eq__(self, other):
            if not isinstance(other, BinarySearchTree.TreeNode):
                return NotImplemented
            return self.__data == other.__data

        def __lt__(self, other):
            if not isinstance(other, BinarySearchTree.TreeNode):
                return NotImplemented
            return self.__data < other.__data

        def __le__(self, other):
            if not isinstance(other, BinarySearchTree.TreeNode):
                return NotImplemented
            return self.__data <= other.__data

        def __gt__(self, other):
            if not isinstance(other, BinarySearchTree.TreeNode):
                return NotImplemented
            return self.__data > other.__data

        def __ge__(self, other):
            if not isinstance(other, BinarySearchTree.TreeNode):
                return NotImplemented
            return self.__data >= other.__data

        def __hash__(self):
            return hash(self.__data)

    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = BinarySearchTree.TreeNode(value)
            return
        current = self.root
        parent = None
        while current:
            parent = current
            if value < current.value:
                current = current.left
            elif value >= current.value:
                current = current.right
        node = BinarySearchTree.TreeNode(value)
        if value < parent.value:
            parent.left = node
        else:
            parent.right = node
        node.parent = current

    def tree_sort(self):
        sorted_list = []
        self.__inorder(self.root, sorted_list)
        return sorted_list

    def __inorder(self, node, lst):
        if node:
            self.__inorder(node.left, lst)
            lst.append(node.data)
            self.__inorder(node.right, lst)
