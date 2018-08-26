from graphs.anagram import anagram_backtracking_word_and_visited, anagram_backtracking_visited
from graphs.anagram import anagram, anagram_immutable
from collections import Counter
import sys

print('############################')
print('Testing anagram_backtracking')
print('############################')

def factorial(n):
    def factorial_iter(prod, n):
        if n == 0:
            return prod

        return factorial_iter(prod * n, n - 1)

    return factorial_iter(1, n)

def count_anagrams(string):
    letters = Counter(string)

    duplicate_permutations = sum(factorial(count) for count in letters.values() if count > 1)

    permutations = factorial(len(string))

    if not duplicate_permutations:
        return permutations

    return permutations / duplicate_permutations


def test(func, string):
    print('############################')
    print("Testing {}('{}')".format(func.__name__, string))
    print('############################')

    assert count_anagrams(string) == len(func(string))


for f in [anagram_backtracking_word_and_visited, anagram_backtracking_visited, anagram, anagram_immutable]:
    for s in ['abd', 'abbbbbbbd']:
        test(f, s)