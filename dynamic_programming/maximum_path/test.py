from trees.binary_tree import BinaryTree
from dynamic_programming.maximum_path.tree import tree_top_down
from dynamic_programming.maximum_path.triangle_graph import triangle_top_down, triangle_top_down_with_cache
from dynamic_programming.maximum_path.triangle_graph import triangle_bottom_up
import copy

print('############################')
print('Testing top_down')
print('############################')

tree = BinaryTree([2,4,2,67,3,3,6,9,7])

tree.prettyPrint()

assert tree_top_down(tree._root) == 83


print('############################')
print('Testing triangle_top_down')
print('############################')

triangle = [[1], [2,3], [4,2,5], [5,1,9,2]]

assert triangle_top_down(triangle) == 9 + 5 + 3 + 1

triangle.append([13, 1, 1, 1, 1])

assert triangle_top_down(triangle) == 13 + 5 + 4 + 2 + 1

print('############################')
print('Testing triangle_top_down_with_cache')
print('############################')

triangle = [[1], [2,3], [4,2,5], [5,1,9,2]]

assert triangle_top_down_with_cache(triangle) == 9 + 5 + 3 + 1

triangle.append([13, 1, 1, 1, 1])

assert triangle_top_down_with_cache(triangle) == 13 + 5 + 4 + 2 + 1

print('############################')
print('Testing triangle_bottom_up')
print('############################')

triangle = [[1], [2,3], [4,2,5], [5,1,9,2]]

result = triangle_bottom_up(copy.deepcopy(triangle))
assert result == 9 + 5 + 3 + 1, "Received {}; expected {}".format(result, 18)

# triangle.append([13, 1, 1, 1, 1])

# assert triangle_bottom_up(copy.deepcopy(triangle)) == 13 + 5 + 4 + 2 + 1