from graphs.minimum_depth_search import minimum_depth

'''
    3
   / \
  9  20
    /  \
   15   7
'''
BINARY_TREE = {
  'val': 3,
  'left': {
    'val': 9,
    'left': None,
    'right': None
  },
  'right': {
    'val': 20,
    'left': {
      'val': 15,
      'left': None,
      'right': None
    },
    'right': {
      'val': 7,
      'left': None,
      'right': None
    }
  }
}

print('############################')
print('Testing minimum_depth_search')
print('############################')

min = minimum_depth(BINARY_TREE)
assert min == 2, "Tree should have minimum depth of 2 and instead got %r" % min