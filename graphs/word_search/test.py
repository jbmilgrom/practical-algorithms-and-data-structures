from graphs.word_search.method import exists, exists_stack_based

print('############################')
print('Testing word_search_backtracking')
print('############################')


boards = [
    {
        'board': [
            ['A', 'B', 'C', 'E'],
            ['S', 'F', 'C', 'S'],
            ['A', 'D', 'E', 'E']
        ],
        'in': ['ABCCED', 'SEE'],
        'out': ['ABCB']
    },
    {
        'board':   [
            ['a', 'a']
        ],
        'in': ['aa'],
        'out': ['aaa']
    }
]

def test(fn):
    for board in boards:
        for word in board['in']:
            assert fn(board['board'], word), "{}({}) is in the board".format(fn.__name__, word)
        for word in board['out']:
            assert not fn(board['board'], word), "{}({}) is NOT in the board".format(fn.__name__, word)

test(exists)
test(exists_stack_based)
