# Problem:
#   Given an array of digits e.g.
#       ['7365', '8342', '1321', '2389']
#   each entry representing a turn of n slot machine wheels, where n is the length of the string
#   and where
#       i. the n wheels are spun independently
#       ii. each digit in each entry corresponds to a different wheel
#       iii. the wheels can change positions per entry
#       ii. each wheel is independently fashioned with up to 9 digits: 1-9
#   determine the least total number of digits required to fashion all n wheels
# Understanding:
#   The least number of total digits required to fashion n wheels occurs when the largest digit in each
#   row/entry is attributed to the same wheel
#
# Plan:
#   STAMPED_OUT = 'STAMPED_OUT'
#   grid_max
#   for every row in grid:
#       row_max, row_max_coord
#       for every digit in row:
#           if digit is STAMPED_OUT:
#               continue
#
#           if digit > row_max:
#               row_max, row_max_coord = digit, (row, digit)
#
#       grid[row_max_coord] = STAMPED_OUT
#       grid_max = max(grid_max, row_max)
#
#   Do this^ n times and add up all the grid maxs
#
#  This is O(n^2)
#  Relatedly, each subsequent iteration through the grid appears wasteful
#
# Plan2 0(log(n)):
#   [Find the 0..n maximum values with a single iteration through the grid]
#   sort each row
#   maximums = grid[0]
#   Now, we can compare apples to apples
#       if row2[i] > row2[i], take row2[i]
#       do this for every i in every row

def minimum_wheel_construction(grid):
    grid_maximums = [0] * len(grid[0])

    for row in grid:
        candidate = list(row)
        candidate.sort()

        for j, digit in enumerate(candidate):
            grid_maximums[j] = max(grid_maximums[j], int(digit))

    return sum(grid_maximums)


print('############################')
print('Testing minimum_wheel_construction')
print('############################')

grid = ['7365', '8342', '1321', '2389']
expected = 9 + 8 + 5 + 3
received =  minimum_wheel_construction(grid)
assert received == expected, "Received {}; expected {}".format(expected, received)

grid = ['7365', '8342', '1321', '2389', '4444']
expected = 9 + 8 + 5 + 4
received =  minimum_wheel_construction(grid)
assert received == expected, "Received {}; expected {}".format(expected, received)