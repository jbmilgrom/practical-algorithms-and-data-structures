from stacks.queue import Queue

'''
Initialize a queue with root
Handle first item in queue while queue has items
  node = q.dequeue()
  doSomething(node)
  for child in node.children(), picking of children L to R (or R to L),
    q.enqueue(child)
'''
def breadth_first_search(root, isItem):
  queue = Queue()
  queue.enqueue(root)
  while not queue.is_empty():
    node = queue.dequeue()
    if isItem(node['val']):
      return True
    try:
      for child in node['children']:
        queue.enqueue(child)
    except KeyError:
      continue
  return False


