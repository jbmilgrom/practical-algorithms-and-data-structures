# Understanding:
#   Example game board: "L_R_"
#   L's can move left; R's can move right
#   We want to know whether one game board is a possible game state of another starting game board
#   An R < R would be a problem; An L > L would also be a problem
# Plan:
#   Iterate through start pushing (i, L/R) onto stack
#   Iterate through end pushing (i, L/R) onto separate stack
#   Pop an item off of each,
#       if L0 < L1: return false
#       if R0 > R1: return false
#       return len(endStack) == 0
def is_game_possible_stack(start, end):
    start_stack, end_stack = [], []

    for i, char in enumerate(start):
        if char == 'L' or char == 'R':
            start_stack.append((char, i))

    for i, char in enumerate(end):
        if char == 'L' or char == 'R':
            end_stack.append((char, i))

    while len(start_stack):
        start_char, start_i = start_stack.pop()
        end_char, end_i = end_stack.pop()

        if end_char != start_char:
            return False

        if end_char == 'R' and end_i < start_i:
            return False

        if end_char == 'L' and end_i > start_i:
            return False

    return len(end_stack) == 0

