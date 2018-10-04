from method import is_game_possible_stack


print('############################')
print('Testing is simple pawn game end state possible')
print('############################')

start = "R  L R L L   L"
possible = " RL  RLL L"
impossible = "R L L RLL"

assert is_game_possible_stack(start, possible)
assert not is_game_possible_stack(start, impossible)