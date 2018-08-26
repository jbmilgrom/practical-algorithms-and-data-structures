# (2 - 1 - 1):
    # ((2 - 1) - 1) => 0
    # (2 - (1 - 1)) => 2
    # returns [0, 2] # order is unimportant
# (2 * 3 - 4 * 5):
    # ((2 * 3) - (4 * 5)) => -14
    # ((2 * (3 - 4)) * 5) => -10
    # (((2 * 3) - 4) * 5) => 10
    # (2 * (3 - (4 * 5))) => -34
    # (2 * ((3 - 4) * 5) => -10
    # returns [-14, -10, 10, -34, -10] # notice the duplicate, order is unimportant
# Notes
  # Every group i.e () can be added to adjacent groups e.g. ((2 * 3) - (4 * 5))
# def permute_order_arithmetic_expr(expr):

