from stacks.queue import Queue

'''
Ideas:
  Execute breadth first search
  When an end is found, return depth
Steps:
  Store number of levels traversed
  BFS:
    While queue has items
      dequeue item and check for children
      if has children, ++levels
      if doesn't have children, return level
'''
def minimum_depth(root):
  q = Queue()
  q.enqueue(root)
  level = 0
  while not q.is_empty():
    level += 1
    node = q.dequeue()
    left, right = node['left'], node['right']
    if left is None and right is None:
      return level
    if left is not None:
      q.enqueue(left)
    else:
      q.enqueue(right)
