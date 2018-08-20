from graphs.minimum_depth_search import minimum_depth_breadth_first, minimum_depth_depth_first

'''
    3
   / \
  9  20
    /  \
   15   7
'''
BINARY_TREE_1 = {
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

BINARY_TREE_2 = {
  'left': {
    'left': {
      'left': {
        'left': None,
        'right': {
          'left': None,
          'right': None,
          'val': 2
        },
        'val': 2
      },
      'right': {
        'left': None,
        'right': {
          'left': None,
          'right': None,
          'val': 4
        },
        'val': 3
      },
      'val': 3
    },
    'right': None,
    'val': 6
  },
  'right': {
    'left': None,
    'right': {
      'left': None,
      'right': None,
      'val': 67
    },
    'val': 9
  },
  'val': 7
}


print('############################')
print('Testing minimum_depth_breadth_first')
print('############################')

min = minimum_depth_breadth_first(BINARY_TREE_1)
assert min == 2, "Tree should have minimum depth of 2 and instead got %r" % min

min = minimum_depth_breadth_first(BINARY_TREE_2)
assert min == 3, "Tree should have minimum depth of 3 and instead got %r" % min


print('############################')
print('Testing minimum_depth_depth_first')
print('############################')

min = minimum_depth_depth_first(BINARY_TREE_1)
assert min == 2, "Tree should have minimum depth of 2 and instead got %r" % min

min = minimum_depth_depth_first(BINARY_TREE_2)
assert min == 3, "Tree should have minimum depth of 3 and instead got %r" % min