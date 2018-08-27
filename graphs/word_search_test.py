from graphs.word_search import exists

print('############################')
print('Testing word_search_backtracking')
print('############################')


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

assert exists(board, 'ABCCED'), "ABCCED is in the board"
assert exists(board, 'SEE'), "SEE is in the board"
assert not exists(board, 'ABCB'), 'ABCB is NOT in the board'
