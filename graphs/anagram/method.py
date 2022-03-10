from collections import Counter

'''
All of these methods generate all anagrams of an inputted string
They have in common the fact that no process is iterative i.e. no process
    carries the complete state of where in the "iteration" the process stands from function call to function call
    can be paused
(Note: the complete state of this graph traversal problem would include the extent which the graph has been traversed
    i.e. a representation of the graph itself)
Instead, each process relies on the call stack to some extent (or stack data structure if reimplemented that way)
    to know where in the graph a given step resides
'''

# anagram_backtracking_word_and_visited
# Understanding:
#   An anagram is a sentence comprised of the same letters from the source, just rearranged
#       It may have more spaces than the original - we are ignoring this fact for now
#       Duplicate letters should also duplicated
# Problem:
#   Given a string of words and spaces, return an array of all valid permutations
# Plan:
#   Graph
#       [L1, L2, ... LN] -> [L1, L2, ... LN-1]
#   Depth first search in order to build up sentences one at time
#   Backtrack on sentence in order to be able to track a single sentence at a time (constant space)

def anagram_backtracking_word_and_visited(sentence):
    length, an_anagram, letters, results = len(sentence), '', Counter(sentence), []

    def recurse_graph():
        nonlocal an_anagram

        if is_last_word_invalid(an_anagram):
            return

        if len(an_anagram) == length:
            results.append(an_anagram)
            return

        for letter, count in letters.items():
            if count == 0:
                continue

            an_anagram += letter
            letters[letter] -= 1
            recurse_graph()
            letters[letter] += 1
            an_anagram = an_anagram[:-1]

    recurse_graph()
    return results

# new string for every node
def anagram_backtracking_visited(sentence):
    length, letters, results  = len(sentence), Counter(sentence), []

    def recurse_graph(_sentence):
        if is_last_word_invalid(_sentence):
            return

        if len(_sentence) == length:
            results.append(_sentence)
            return

        for letter, count in letters.items():
            if not count:
                continue

            letters[letter] -= 1
            recurse_graph(_sentence + letter)
            letters[letter] += 1

    recurse_graph('')
    return results

# new string for every node
# dictionary representing the history of _un_visited nodes for every node
def anagram(sentence):
    length, results = len(sentence), []
    def recurse_tree(remaining_letters, _sentence):
        if is_last_word_invalid(_sentence):
            return

        if len(_sentence) == length:
            results.append(_sentence)
            return

        for letter, count in remaining_letters.items():
            if not count:
                continue

            copy = remaining_letters.copy()
            copy[letter] -= 1
            recurse_tree(copy, _sentence + letter)

    recurse_tree(Counter(sentence), '')
    return results

# Avoid shared state between function calls
def anagram_immutable(sentence):
    length = len(sentence)
    def recurse_tree(remaining_letters, _sentence):
        if is_last_word_invalid(_sentence):
            return []

        if len(_sentence) == length:
            return [_sentence]

        results = []
        for letter, count in remaining_letters.items():
            if not count:
                continue

            copy = remaining_letters.copy()
            copy[letter] -= 1
            results = results + recurse_tree(copy, _sentence + letter)
        return results

    return recurse_tree(Counter(sentence), '')

# Trivial for now
def is_last_word_invalid(word):
    return False
