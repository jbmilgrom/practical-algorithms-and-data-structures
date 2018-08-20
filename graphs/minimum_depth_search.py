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
def minimum_depth_breadth_first(root):
  if not root:
    return 0
  q = Queue()
  q.enqueue((root, 1))
  while not q.is_empty():
    node, level = q.dequeue()
    left, right = node['left'], node['right']
    if not left and not right:
      return level
    if left:
      q.enqueue((left, level + 1))
    if right:
      q.enqueue((right, level + 1))

'''
The depth of a leaf-node is 1
The minimum depth of a tree equals 1 plus the min of the minimum depths of its childen subtrees
'''
def minimum_depth_depth_first(root):
  if not root:
    return 0
  left, right, SINGLE_NODE_DEPTH = root['left'], root['right'], 1
  if not left and not right:
    return SINGLE_NODE_DEPTH
  if left and right:
    return SINGLE_NODE_DEPTH + min(minimum_depth_depth_first(left), minimum_depth_breadth_first(right))
  return SINGLE_NODE_DEPTH + minimum_depth_breadth_first(left or right)
