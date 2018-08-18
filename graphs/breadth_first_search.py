from stacks.queue import Queue

def breadth_first_search(root, isItem):
  queue = Queue()
  queue.enqueue(root)
  while not queue.is_empty():
    node = queue.dequeue()
    if isItem(node.val):
      return True
    for childNode in node.children:
      queue.enqueue(childNode)
  return False


TREE = {
  'val': 'A',
  'children': [
      {
          'val': 'B',
          'children': [
              {'val': 'D'},
              {'val': 'E'},
          ]
      },
      {
          'val': 'C',
          'children': [
              {'val': 'F'},
              {'val': 'G'},
              {'val': 'H'}
          ]
      }
  ]
}

def isItem(item):
  return item == 'F'
print(breadth_first_search(TREE, isItem))





