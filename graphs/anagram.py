from collections import Counter

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
#   Backtrack on sentence in order to be able to track a single sentence at a time
def anagram_backtracking(sentence):
    length = len(sentence)
    results = []
    an_anagram = ''
    letters = Counter(sentence)
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
            an_anagram = an_anagram[:-1]
            letters[letter] += 1
    recurse_graph()
    return results

# Trivial for now
def is_last_word_invalid(word):
    return False
