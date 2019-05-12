"""A simple queue - FIFO implementation that has fixed number of slots. Each slot
can hold any object
"""
DEFAULT_QUEUE_SIZE = 10


class Queue:
    """Queue has fixed number of slots and each slot can hold any object.
If the number of slots is not passed or invalid value, queue defaults to
DEFAULT_QUEUE_SIZE."""

    def __init__(self, max_slots=DEFAULT_QUEUE_SIZE):
        if not isinstance(max_slots, int) or max_slots < 1:
            self.max_slots = DEFAULT_QUEUE_SIZE
        else:
            self.max_slots = max_slots
        self._container = []

    def add(self, an_object):
        """Add an object if queue is not full"""
        if len(self._container) >= self.max_slots:
            raise QueueOverflow("Queue is full")

        self._container.append(an_object)

    def retrieve(self):
        """Remove and get the first inserted item if the queue is not empty"""
        if not self._container:
            raise QueueUnderflow("Queue is empty")

        return self._container.pop(0)

    def __contains__(self, item):
        return item in self._container

    def __len__(self):
        return len(self._container)

    def clear(self):
        """Clears the queue"""
        return self._container.clear()


class QueueOverflow(Exception):
    """Indicates that the queue is full"""
    def __init__(self, message):
        super(QueueOverflow, self).__init__(message)
        self.message = message


class QueueUnderflow(Exception):
    """Indicates that the queue is empty"""
    def __init__(self, message):
        super(QueueUnderflow, self).__init__(message)
        self.message = message