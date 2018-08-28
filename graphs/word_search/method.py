from stacks.stack import Stack

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

    def has_word(index, current):
        if board[current[0]][current[1]] is not word[index]:
            return

        if index + 1 == length:
            return True

        # Build up a history of the path to avoid backtracking/double-counting e.g. A (0, 1) -> B (0, 2) -> B (0, 1)
        #   This isn't to avoid an infinite loop - letters that are not on the board cannot be found; this is
        #   only to avoid false positives e.g. ABA
        visited.add(current)

        for next in neighbors(current, n, m):
            if next in visited:
                continue

            if has_word(index + 1, next):
                return True

        # We are diving into the depths of the graph to locate a word
        # If the dive (root) didn't work remove the root and try a different dive
        visited.remove(current)

    for i in range(0, n):
        for j in range(0, m):
            if has_word(0, (i, j)):
                return True

    return False

# Understanding:
#   Depth first search with a stack:
#       Push children onto the stack
#       Pop node from stack, and get children
#           Limit the children to unvisited
#  Problem:
#   Find whether a certain sequence of characters can be found on the board

def exists_stack_based(board, word):
    visited, n, m, length = set(), len(board), len(board[0]), len(word)

    def has_word(current):
        index, stack = 0, Stack()
        stack.push(current)

        while not stack.is_empty():
            current = stack.pop()

            if current[0] == 'PARENT_MARKER':
                visited.remove(current[1])
                index -= 1
                continue

            if board[current[0]][current[1]] is not word[index]:
                continue

            if index + 1 == length:
                return True

            visited.add(current)
            index += 1

            # Mark the parent of the below children so that if all children are processed and no word is found,
            # we can remove the parent from visited as well and move onto the remaining items in the stack
            stack.push(('PARENT_MARKER', current))

            for next in neighbors(current, n, m):
                if next in visited:
                    continue

                stack.push(next)

        return False

    for i in range(0, n):
        for j in range(0, m):
            if has_word((i, j)):
                return True

    return False

def neighbors(coordinate, n, m):
    low = -1
    x, y = coordinate
    delta = [ (0, 1), (1, 0), (-1, 0), (0, -1) ]
    return [ (x + i, y + j) for i, j in delta if x + i < n and x + i > low and y + j < m and y + j > low ]
