# Understanding
#   We are looking for a contiguous subarray that sums to a larger amount than any other subarray
#   If all numbers are positive, the largest subarray is the array itself
#   If all numbers are negative, the largest subarray is the least negative number by itself
#   n^2 iteration could build each sum
#   The max of (the max subarray of each of 0...n-1) gives the answer
# def maximum_subarray(arr):


# def maximum_subarray_that_ends_at(i, arr):
