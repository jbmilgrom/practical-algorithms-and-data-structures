# Understanding:
#   An island consists of connected 1's,
#     the perimeter of which is 0's on all N,S,E,W (or terroritory end) sides
#   The ocean consists of 0's
#   Given a matrix of 1s & 0s, return the number of islands
# Insight:
#   Every 1 is an island, unless connected to another 1
# Plan:
#   Track total islands
#   Start at (0, 0)
#   Algo:
#     Linearly search until land is found
#     DFS, stamping out land.
#     Increment total
#     Repeat

# def count_islands(matrix):
#   islands = 0
#   i, j = 0, 0
#   while i < matr:
