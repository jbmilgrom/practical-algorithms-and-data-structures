from graphs.breadth_first_search import breadth_first_search
from graphs.depth_first_search import depth_first_search, depth_first_search_recursive

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
        {
          'val': 'H',
          'children': [
            {'val': 'K'}
          ]
        }
      ]
    }
  ]
}

items = ['A', 'F','G','H','C','B','D','K']
non_items = ['I', 'J','X','Z','M','N']

print('############################')
print('Testing breadth_first_search')
print('############################')

for letter in items:
  assert breadth_first_search(TREE, lambda x: x == letter), "Letter %r should be in the graph" % letter

for letter in non_items:
  assert not breadth_first_search(TREE, lambda x: x == letter), "Letter %r should not be in the graph" % letter

print('############################')
print('Testing depth_first_search')
print('############################')

for letter in items:
  assert depth_first_search(TREE, lambda x: x == letter), "Letter %r should be in the graph" % letter

for letter in non_items:
  assert not depth_first_search(TREE, lambda x: x == letter), "Letter %r should not be in the graph" % letter

print('############################')
print('Testing depth_first_search_recursive')
print('############################')

for letter in items:
  assert depth_first_search_recursive(TREE, lambda x: x == letter), "Letter %r should be in the graph" % letter

for letter in non_items:
  assert None == depth_first_search_recursive(TREE, lambda x: x == letter), "Letter %r should not be in the graph" % letter