"""A simple stack implementation with push and pop of objects with stack containing
fixed number of slots
"""

DEFAULT_STACK_SIZE = 10


class Stack:
    """Stack that implements push and pop. The stack has a default number of slots which
can be overridden while instantiation"""
    def __init__(self, max_slots=DEFAULT_STACK_SIZE):
        if not isinstance(max_slots, int) or max_slots < 1:
            self.max_slots = DEFAULT_STACK_SIZE
        else:
            self.max_slots = max_slots
        self._container = []

    def push(self, an_object):
        """Pushes an object to the stack when stack is not full"""
        if len(self._container) >= self.max_slots:
            raise StackOverflow("Stack is full")

        return self._container.append(an_object)

    def pop(self):
        """Pops the last inserted object when the stack is not empty"""
        if not self._container:
            raise StackUnderflow("Stack is empty")

        return self._container.pop(len(self._container) - 1)

    def __len__(self):
        return len(self._container)

    def __contains__(self, item):
        return item in self._container


class StackOverflow(Exception):
    """Exception indicates that the stack is full"""
    def __init__(self, message):
        super(StackOverflow, self).__init__(message)
        self.message = message


class StackUnderflow(Exception):
    """Exception indicates that the stack is empty"""
    def __init__(self, message):
        super(StackUnderflow, self).__init__(message)
        self.message = message