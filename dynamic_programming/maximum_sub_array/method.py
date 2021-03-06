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
    maximum = None

    for i, num in enumerate(nums):
        if i == 0:
            previous = maximum = num
            continue

        previous = max(num + previous, num)
        maximum = max(previous, maximum)

    return maximum

# recursive procedure to perform iteration
def maximum_subarray_rec_proc(nums):
    def iterate(i, maximum, previous):
        if i == len(nums):
            return maximum

        num = nums[i]
        previous = max(num + previous, num)
        return  iterate(i + 1, max(previous, maximum), previous)

    return iterate(1, nums[0], nums[0])





