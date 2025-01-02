from typing import Any, Iterator


class Stack:
    class UnderflowError(Exception):
        def __init__(self, message="Stack underflow error"):
            self.message = message
            super().__init__(self.message)

    def __init__(self):
        self.__stack = []
        self.__top = -1

    @property
    def stack(self):
        return self.__stack

    def push(self, element: Any) -> bool:
        if element is not None:
            self.__top += 1
            self.__stack.append(element)
            return True
        return False

    def pop(self) -> Any:
        if self.is_empty():
            raise Stack.UnderflowError()
        else:
            self.__top -= 1
            previous_top = self.__stack[self.__top + 1]
            del self.__stack[self.__top + 1]
            return previous_top

    def peek(self) -> Any:
        if self.__top > -1:
            return self.__stack[self.__top]
        raise Stack.UnderflowError()

    def is_empty(self) -> bool:
        return self.__top == -1

    def size(self) -> int:
        return len(self.__stack)

    def clear(self) -> None:
        self.__stack.clear()
        self.__top = -1

    def __len__(self) -> int:
        """Return the number of elements in the stack."""
        return self.size()

    def __iter__(self) -> Iterator[Any]:
        """Return an iterator over the stack."""
        return iter(self.__stack)

    def __repr__(self) -> str:
        """Return a string representation of the stack."""
        return f"Stack(top={self.__top}, elements={self.__stack})"

    def __str__(self) -> str:
        """Return a string representation of the stack."""
        return f"Stack: {self.__stack}\n"