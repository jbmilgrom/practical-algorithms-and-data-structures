from dynamic_programming.maximum_sub_array.method import maximum_subarray

print('############################')
print('Testing maximum_sub_array')
print('############################')

max = maximum_subarray([-1, 3,2,6, -3, 4,5])
assert max == 17, "expected {}; received: {}".format(17, max)

max = maximum_subarray([-1, -3, -2, -6, -3, -4, -5])
assert max == -1, "expected {}; received: {}".format(-1, max)

max = maximum_subarray([-9, -3, -2, -6, -3, -4, -5])
assert max == -2, "expected {}; received: {}".format(-2, max)

max = maximum_subarray([-1, 3,2,6, -3, 4,5, 9, -1])
assert max == 26, "expected {}; received: {}".format(26, max)

max = maximum_subarray([-1, 3,2,6, -3, 4,5, 9, -1, 10, 10])
assert max == 45, "expected {}; received: {}".format(45, max)

max = maximum_subarray([-1, 3,2,6, -3, 4,5, 9, -1, 10, 2, 3, -9])
assert max == 40, "expected {}; received: {}".format(40, max)