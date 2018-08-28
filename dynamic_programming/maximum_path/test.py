from trees.binary_tree import BinaryTree
from dynamic_programming.maximum_path.method import maximum_path_top_down

print('############################')
print('Testing maximum_path_top_down')
print('############################')

tree = BinaryTree([2,4,2,67,3,3,6,9,7])

tree.prettyPrint()

print(maximum_path_top_down(tree))