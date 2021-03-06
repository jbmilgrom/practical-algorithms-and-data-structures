from pprint import pprint

class Stack:

  def __init__(self):
    self._items = []

  def is_empty(self):
    return self.size() == 0

  def pop(self):
    return self._items.pop()

  def push(self, item):
    self._items.append(item)

  def peek(self):
    return self._items[-1]

  def size(self):
    return len(self._items)

  def stdout(self):
    pprint(self._items)