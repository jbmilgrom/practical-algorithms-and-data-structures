from stacks.stack import Stack

def depth_first_search(root, isItem):
  s = Stack()
  s.push(root)
  while not s.is_empty():
    node = s.pop()
    if isItem(node['val']):
      return True
    try:
      for child in node['children']:
        s.push(child)
    except KeyError:
      continue
  return False