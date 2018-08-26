from graphs.anagram import anagram_backtracking
from collections import Counter

print('############################')
print('Testing anagram_backtracking')
print('############################')

def factorial(n):
    def factorial_iter(prod, n):
        if n == 0:
            return prod
        return factorial_iter(prod * n, n - 1)
    return factorial_iter(1, n)

def count_results(string):
    letters = Counter(string)
    duplicate_permutations = 0

    for count in letters.values():
        if count > 1:
            duplicate_permutations += factorial(count)

    permutations = factorial(len(string))

    if not duplicate_permutations:
        return permutations

    return permutations / duplicate_permutations


def test(string):
    print('############################')
    print("Testing anagram_backtracking('{}')".format(string))
    print('############################')

    assert count_results(string) == len(anagram_backtracking(string))


test('abd')
test('abbbbbbbd')