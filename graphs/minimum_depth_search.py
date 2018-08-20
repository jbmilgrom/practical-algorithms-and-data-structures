from stacks.queue import Queue
from pprint import pprint

'''
Queue analysis:
  e.g
        3
       / \
      9  20
     / \
    15  7

  while queue [Node3]
    queue is []
    process(Node3)
    enqueue Node9, Node20
  while queue [Node9, Node20]
    queue is [Node20]
    process(Node9)
    enqueue Node15, Node7
  while queue [Node20, Node15, Node7]
    queue is []
    process(Node20)
    enqueue nothing
  while queue [Node15, Node7]
    queue is [Node7]
    process(Node15)
    enqueue nothing
  while queue [Node7]
    queue is []
    process(Node7)
    enqueue nothing
Ideas:
  Execute breadth first search
    But how to the level children are associated with?
      assign levels to nodes
        root node is level 1
        children are parent + 1
      first node without children, level
Steps:
  BFS:
    While queue has items
      dequeue node and return its level if has no children
      otherwise, enqueue node with parent+1 level meta data
'''
def minimum_depth(root):
  if not root:
    return 0
  q = Queue()
  q.enqueue(node_level_pair(root, 1))
  while not q.is_empty():
    node = q.dequeue()
    left, right, level = node['node']['left'], node['node']['right'], node['level']
    if not left and not right:
      return level
    if left:
      q.enqueue(node_level_pair(left, level + 1))
    if right:
      q.enqueue(node_level_pair(right, level + 1))

def node_level_pair(node, level):
  return {'node': node, 'level': level}