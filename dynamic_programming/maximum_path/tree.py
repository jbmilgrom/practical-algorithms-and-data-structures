from trees.binary_tree import BinaryTree

# Understanding:
#   Given a 2^height tree, find the maximum path
#   Depth or Breadth first search will yield the answer but in 2^h time
#   Are there recurring subproblems?
#       Top-down:
#           f(T) = max(f(T.L), f(T.R))
# Problem:
#   Given a list representation of a tree, return the sum of the maximum path
# Plan:
#   Depth first recursive search:
#       Base case: leaf nodes i.e. nodes with no children -> max is trivially the value
#       f(T) = max(f(T.L), f(T.R))

LEFT = BinaryTree.L
RIGHT = BinaryTree.R
VALUE = BinaryTree.V

def tree_top_down(tree):
    if tree[LEFT] is None and tree[RIGHT] is None:
        return tree[VALUE]

    if tree[LEFT] and tree[RIGHT]:
        return tree[VALUE] + max(tree_top_down(tree[LEFT]), tree_top_down(tree[RIGHT]))

    if tree[LEFT]:
        return tree[VALUE] + tree_top_down(tree[LEFT])
    else:
        return tree[VALUE] + tree_top_down(tree[RIGHT])


# def maximum_path_top_down_caching(tree):
#     cache = {}
#     def setCache(k, v):
#         cache[hash(k)] = v

#     def maximum_path_top_down(tree):
#         hit = cache.get(tree)
#         if hit:
#             return hit

#         if tree[LEFT] is None and tree[RIGHT] is None:
#             return tree[VALUE]

#         if tree[LEFT] and tree[RIGHT]:
#             setCache(tree[LEFT], maximum_path_top_down(tree[LEFT]))
#             setCache(tree[RIGHT], maximum_path_top_down(tree[RIGHT]))
#             return tree[VALUE] + max(cache[tree[LEFT]], cache[tree[RIGHT]])

#         direction = LEFT if tree[LEFT] else RIGHT
#         setCache(tree[direction], maximum_path_top_down(tree[direction]))
#         return tree[VALUE] + cache[tree[direction]]

#     return maximum_path_top_down(tree)