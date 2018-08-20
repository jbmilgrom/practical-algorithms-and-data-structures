from graphs.perfect_sqaures import least_perfect_sqaures_that_sum_to

print('############################')
print('Testing least_perfect_sqaures_that_sum_to')
print('############################')

result = least_perfect_sqaures_that_sum_to(13)
assert result == 2, "least_perfect_sqaures_that_sum_to(13) is 2; received %r" % result
result = least_perfect_sqaures_that_sum_to(12)
assert result == 3, "least_perfect_sqaures_that_sum_to(12) is 3; received %r" % result
result = least_perfect_sqaures_that_sum_to(28)
assert result == 4, "least_perfect_sqaures_that_sum_to(28) is 4; received %r" % result