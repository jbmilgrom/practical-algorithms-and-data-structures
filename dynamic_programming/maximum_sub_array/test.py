from dynamic_programming.maximum_sub_array.method import maximum_subarray

print('############################')
print('Testing maximum_sub_array')
print('############################')

max = maximum_subarray([-1, 3,2,6, -3, 4,5])
assert max == 3 + 2 + 6, "expected {}; received: {}".format(11, max)

max = maximum_subarray([-1, -3, -2, -6, -3, -4, -5])
assert max == -1, "expected {}; received: {}".format(-1, max)

max = maximum_subarray([-9, -3, -2, -6, -3, -4, -5])
assert max == -2, "expected {}; received: {}".format(-2, max)

max = maximum_subarray([-1, 3,2,6, -3, 4,5, 9, -1])
assert max == 18, "expected {}; received: {}".format(18, max)

max = maximum_subarray([-1, 3,2,6, -3, 4,5, 9, -1, 10, 10])
assert max == 20, "expected {}; received: {}".format(20, max)

max = maximum_subarray([-1, 3,2,6, -3, 4,5, 9, -1, 10, 2, 3, -9])
assert max == 18, "expected {}; received: {}".format(18, max)