from stack import Stack

class Queue:
  def __init__(self):
    self._items = Stack()

  def enqueue(self, item):
    self._items.push(item)
  
  def dequeue(self):
    temp = Stack()
    while self._items.size() > 0:
      temp.push(self._items.pop())
    item = temp.pop()
    while temp.size() > 0:
      self._items.push(temp.pop())
    return item

q = Queue()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)

print q.dequeue() # 1
print q.dequeue() # 2