from dynamic_programming.house_robber.method import house_robber, robber_robber

houses = [([3, 2, 1, 5, 7], 11), ([3, 10, 1, 5, 7, 3], 18)]
houses_that_rob = [([-4, -4, 5, -2, -7, 8, -2], 13)]

def test(fn, houses):
    for house, sum in houses:
        received = fn(house)
        assert received == sum, "Expected {}; received {}".format(sum, received)

print('############################')
print('Testing house_robber')
print('############################')

test(house_robber, houses)

print('############################')
print('Testing robber_robber')
print('############################')

test(robber_robber, houses + houses_that_rob)