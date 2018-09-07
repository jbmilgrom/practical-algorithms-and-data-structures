from pprint import pprint

class BinaryTree:
  L = 'left'
  R = 'right'
  V = 'val'

  def __init__(self, values, isLeft = lambda x, y: x < y):
    self._isLeft = isLeft
    self._root = self.node(values.pop())
    while len(values) > 0:
      self.insert_node(self.node(values.pop()))

  def depth_first_search(self, val):
    def _search(root, val, isLeft):
      if root is None:
        return False
      if root[self.V] == val:
        return True
      else:
        dir = self.L if isLeft(val, root[self.V]) else self.R
        return _search(root[dir], val, isLeft)

    return _search(self._root, val, self._isLeft)

  def insert_node(self, node):
    # if n.right and n.val >= r.val, traverse right
    #   else r.right = n
    # if n.val < r.val, traverse left
    #   else r.left = n
    def _insert_node(root, node, isLeft):
      dir = self.R
      if isLeft(node[self.V], root[self.V]):
        dir = self.L
      if root[dir]:
        _insert_node(root[dir], node, isLeft)
      else:
        root[dir] = node

    _insert_node(self._root, node, self._isLeft)

  def for_each(self, do):
    def traverse(node, do):
      if node:
        do(node[self.V])
        traverse(node[self.L], do)
        traverse(node[self.R], do)

    traverse(self._root, do)

  def node(self, val, left = None, right = None):
    return {
      self.V: val,
      self.L: left,
      self.R: right
    }

  def prettyPrint(self):
    pprint(self._root, width=1)