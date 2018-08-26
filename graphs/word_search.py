# Understanding:
#   A word can begin anywhere and go in any direction sequentially
#   Valid directions: N, W, S, E
# Problem:
#   Given a word, determine whether or not it can be found in the grid
# Plan:
#   Depth first search the grid, return True when word is found
#     Accrue a word as a path is descended
#     Decrement word as path is ascended
#
#   Otherwise, return False
def word_search(grid, word):
  letters = grid[0][0]
  x_length = len(grid)
  y_length = len(grid[0])
  start = (0, 0)
  visited = {start: True}
  def recurse_grid(coord):
    nonlocal letters
    if word in letters:
      return True
    if len(letters) == y_length * x_length:
      return
    for next in neighbors(coord, -1, x_length, y_length):
      if visited.get(next):
        continue
      letters += grid[next[0]][next[1]]
      visited[next] = True
      has_word = recurse_grid(next)
      if has_word:
        return True
      letters = letters[:-1]
      visited[next] = False
  return recurse_grid(start)

def neighbors(coordinate, low, x_high, y_high):
  x, y = coordinate
  delta = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]
  return [ (x + i, y + j) for i, j in delta if x + i < x_high and x + i > low and y + j < y_high and y + j > low ]
