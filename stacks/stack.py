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

stack = Stack()
stack.push(4)
print stack.peek()
print stack.size()
print stack.is_empty()
stack.push(5)
print stack.peek()
print stack.size()
print stack.is_empty()
stack.pop()
print stack.peek()
print stack.size()
print stack.is_empty()