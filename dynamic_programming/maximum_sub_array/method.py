# Understanding
#   We are looking for a contiguous subarray that sums to a larger amount than any other subarray
#   If all numbers are positive, the largest subarray is the array itself
#   If all numbers are negative, the largest subarray is the least negative number by itself
#   n^2 iteration could build each sum
#   The max of (the max subarray of each of 0...n-1) gives the answer
# Insight:
#   Find the maximum subarray that ends at i
#   Add i + 1
# Understanding:
#   The maximum subarray that ends at i + 1 is:
#       the maximum subarrary plus i if i > 0 and array ends at i
#       elif i < 0: do nothing
#       elif subarray[i] == None: check subarray ending at i against max
# Problem:
#   Given an array of integers, return the max sum of aany contiguous subarray
def maximum_subarray(arr):
    max, end, alternative_max = arr[0], 0, None

    for i in range(1, len(arr)):
        num = arr[i]

        # if max is less than zero, we have easy work to do
        if max < 0 and num > max:
            max, end = num, i
            continue

        # if num is less than zero (and max isn't), move on
        if num < 0:
            continue

        # if max subarray is alive (and num > 0), add to it and keep it alive
        if end == i - 1:
            max, end = max + num, i
            continue

        # otherwise, build an alternative
        alternative_max = num if alternative_max is None else alternative_max + num

        # if the alternative is greater than the max, we have a new max, remove the alternative
        if alternative_max > max:
            max, alternative_max, end = alternative_max, None, i

    return max



