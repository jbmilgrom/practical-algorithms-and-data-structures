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

'''
Steps:
  Root is checked for item
  The left-most child is checked for item
  The left-most child's left-most child is checked for item
  ...
  If item is not found in the left-most branch's leaf-node
  The leftest leaf-node's parent's next leftest child is checked
  ...
  If item is not found in the leftest leaf-node's parent's next leftest branch's leaf-node
  And the leftest leaf-node's parent has no more children
  The leftest leaf-node's grandparent's next leftest child is checked
  ...

The Call _Stack_ Stores "Next Node" Instructions:
When a branch is exhausted, the function call to the leaf node returns and is
popped from the call stack, and the remainder of the call stack is summoned for further
instruction. If the recursive process has been correctly designed, requests to children
of increasingly senior nodes lay in wait as was all as increasingly junior nodes
with respect thereto.
'''
def depth_first_search_recursive(root, isItem):
  if isItem(root['val']):
    return True
  try:
    for child in root['children']:
      has_item = depth_first_search_recursive(child, isItem)
      if has_item:
        return True
  except KeyError:
    return False