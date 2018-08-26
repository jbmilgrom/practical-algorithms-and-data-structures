from stacks.stack import Stack

class Queue:
  def __init__(self):
    self._enqueue = Stack()
    self._dequeue = Stack()

  def is_empty(self):
    return self._enqueue.is_empty() and self._dequeue.is_empty()

  def size(self):
    return self._dequeue.size() + self._enqueue.size()

  def enqueue(self, item):
    self._enqueue.push(item)

  def dequeue(self):
    if self._dequeue.is_empty():
      while not self._enqueue.is_empty():
        self._dequeue.push(self._enqueue.pop())
    return self._dequeue.pop()

  def stdout(self):
    print('_enqueue')
    self._enqueue.stdout()
    print('_dequeue')
    self._dequeue.stdout()