from graphs.breadth_first_search import breadth_first_search

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

print(breadth_first_search(TREE, lambda x: x == 'F'))
print(breadth_first_search(TREE, lambda x: x == 'G'))
print(breadth_first_search(TREE, lambda x: x == 'H'))
print(breadth_first_search(TREE, lambda x: x == 'C'))
print(breadth_first_search(TREE, lambda x: x == 'B'))
print(breadth_first_search(TREE, lambda x: x == 'D'))

print(breadth_first_search(TREE, lambda x: x == 'J'))
print(breadth_first_search(TREE, lambda x: x == 'K'))