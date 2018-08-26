from graphs.word_search import word_search

print('############################')
print('Testing word_search')
print('############################')


board = [
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

print(word_search(board, 'ABCCED'))

# assert word_search(board, 'ABCCED'), "ABCCED is in the board"
assert word_search(board, 'SEE'), "SEE is in the board"
# assert None == word_search(board, 'ABCB'), 'ABCB is NOT in the board'