from collections import Counter

# Problem:
#   given a list of numbers e.g. [2,1,4,6,2], find the number of unique pairs that sum to k
#   note 4 + 2 is the same as 2 + 4
# Understanding:
#   Brute force iteration can generate all pairs (i, j)
#   Turn arr into dictionary of counts and look for pair directly
# Plan:
#   make a dictionary out of the nums
#   iterate through the dictionary keys and search for counterparts incremementing a total if found
#   Keep a set of pairs to avoid duplicates
def num_of_pair_sums(arr, k):
    nums, total, pairs = Counter(arr), 0, set()

    for num in nums:
        counterpart = k - num
        pair = (max(num, counterpart), min(num, counterpart))

        if nums.get(counterpart) and pair not in pairs:
            pairs.add(pair)
            total+=1

    return total


print('############################')
print('Testing num_of_pair_sums')
print('############################')

nums = [2,1,4,6,2]
received = num_of_pair_sums(nums, 6)
expected = 1
assert received == expected, "received {}; expected {}".format(received, expected)

nums = [2,1,4,6, 2, 0, 2, 3, 3, 5, 1]
received = num_of_pair_sums(nums, 6)
expected = 4
assert received == expected, "received {}; expected {}".format(received, expected)