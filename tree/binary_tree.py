from pprint import pprint

class BinaryTree:
  def __init__(self, values, isLeft = lambda x, y: x < y):
    self._isLeft = isLeft
    self._root = self.node(values.pop())
    for v in values:
      self.insert_node(self.node(v))

  def search(self, val):
    def _search(root, val, isLeft):
      if root is None:
        return False
      if root['val'] == val:
        return True
      else:
        dir = 'left' if isLeft(val, root['val']) else 'right'
        return _search(root[dir], val, isLeft)

    return _search(self._root, val, self._isLeft)

  def insert_node(self, node):
    # if n.right and n.val >= r.val, traverse right
    #   else r.right = n
    # if n.val < r.val, traverse left
    #   else r.left = n
    def _insert_node(root, node, isLeft):
      dir = 'right'
      if isLeft(node['val'], root['val']):
        dir = 'left'
      if root[dir] is not None:
        _insert_node(root[dir], node, isLeft)
      else:
        root[dir] = node

    _insert_node(self._root, node, self._isLeft)

  def for_each(self, do):
    def traverse(node, do):
      if node:
        do(node['val'])
        traverse(node['left'], do)
        traverse(node['right'], do)

    traverse(self._root, do)

  def node(self, val, left = None, right = None):
    return {
      'val': val,
      'left': left,
      'right': right
    }

  def prettyPrint(self):
    pprint(self._root)