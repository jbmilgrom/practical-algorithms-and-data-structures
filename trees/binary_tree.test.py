from binary_tree import BinaryTree

items = [2,4,2,67,3,3,6,9,7]
tree = BinaryTree(list(items))
tree.prettyPrint()

for i in items:
  assert tree.depth_first_search(i), "%r should be in tree but cannot be found" % i
print("tree.search identifies leaves on the tree")

nonItems = [-1,0,1,5,8,10,23, 96]

for j in nonItems:
  assert not tree.depth_first_search(j), "%r is not in tree and can be found" % j
print("tree.search identifies leaves that are not on the tree")