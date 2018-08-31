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
#   The max of subarray that endssss in i
#   If we know the max subarray that endsss at n - 1, then we know the max subarray that ends at n
#       if is max(n-1 + n, n)
# Problem:
#   Given an array of integers, return the max sum of aany contiguous subarray
def maximum_subarray(nums):
    all = [None] * len(nums)

    for i, num in enumerate(nums):
        if i == 0:
            all[0] = num
            continue

        all[i] = max(num + all[i - 1], num)

    return max(all)






