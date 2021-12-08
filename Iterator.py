import random


def generator(number, left, right):
    while number > 0:
        number = number - 1
        yield random.randint(left, right)


class Iterator:

    def __iter__(self):
        return self

    def __init__(self, number, left, right):
        self._number = number
        self._left = left
        self._right = right
        self._counter = 0

    def __next__(self):
        if self._counter < self._number:
            self._counter = self._counter + 1
            return random.randint(self._left, self._right)
        else:
            raise StopIteration
