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

def depth_first_search_recursive(root, isItem):
  if isItem(root['val']):
    return True
  try:
    for child in root['children']:
      has_item = depth_first_search_recursive(child, isItem)
      if has_item:
        return True
  except KeyError:
    # if we've arrived at the end of a branch with no children, it doesnt have the item
    return False