# Understanding:
#   n x m board with a letter in each slot
#   Board can be traversed N, S, E, W
#   A "word" is a sequence of letters
# Problem:
#   Given a word, determine is a matching sequence exists in the board
# Graph:
#   Given a point (i, j) on the board, a graph constitutes paths in all directions therefrom
#   (i, j) -> N, S, W, E
#   where a node is considered visited when touched and part of a successful match
# Plan:
#   Iterate through each m x n spot on the graph
#   Depth first search(globally maintained visited set with backtracking)
#       terminate if letter doesn't match
#       continue if letter matches, stopping when a length of path equals len(word), return True
def exists(board, word):
    visited, n, m, length = set(), len(board), len(board[0]), len(word)

    def traverse(index, current):
        if board[current[0]][current[1]] is not word[index]:
            return

        if index + 1 == length:
            return True

        visited.add(current)

        for next in neighbors(current, n, m):
            if next in visited:
                continue

            has_word = traverse(index + 1, next)
            if has_word:
                return True

        visited.remove(current)

    for i in range(0, n):
        for j in range(0, m):
            has_word = traverse(0, (i, j))
            if has_word:
                return True

    return False


def neighbors(coordinate, n, m):
    low = -1
    x, y = coordinate
    delta = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]
    return [ (x + i, y + j) for i, j in delta if x + i < n and x + i > low and y + j < m and y + j > low ]
