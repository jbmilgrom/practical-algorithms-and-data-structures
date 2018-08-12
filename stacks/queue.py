from stack import Stack

class Queue:
  def __init__(self):
    self._enqueue = Stack()
    self._dequeue = Stack()

  def is_empty(self):
    return self.is_empty() and self.is_empty()

  def size(self):
    return self._dequeue.size() + self._enqueue.size()

  def enqueue(self, item):
    self._enqueue.push(item)
  
  def dequeue(self):
    if self._dequeue.is_empty():
      while not self._enqueue.is_empty():
        self._dequeue.push(self._enqueue.pop())
    return self._dequeue.pop()

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print q.dequeue() # 1
print q.dequeue() # 2

q.enqueue(4)

print q.dequeue() # 3
print q.dequeue() # 4