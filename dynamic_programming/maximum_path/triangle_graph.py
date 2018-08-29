# Understanding:
#   f(i, j) = arr[i, j] +  max( f(i+1, j), f(i+1, j+1) )
#   Depth first search of the triangle
#       Neighbors are determined by (i +1, j), (i +1, j + 1)
#       Base condition is a leaf node determined by running out of rows
# Problem:
#   Given an array of arrays representing a triangle e.g. [[1], [2, 3], [4,2,6]], return sum of maximum path
def triangle_top_down(arr):
    height = len(arr)

    def get_max(i, j):

        if not in_equilateral_triangle(height, i, j):
            return 0

        return arr[i][j] + max(get_max(i + 1, j), get_max(i + 1, j + 1))

    return get_max(0, 0)


def triangle_top_down_with_cache(arr):
    height, cache = len(arr), {}

    def get_max(i, j):
        hit = cache.get((i, j))
        if hit:
            return hit

        if not in_equilateral_triangle(height, i, j):
            return 0

        result = arr[i][j] + max(get_max(i + 1, j), get_max(i + 1, j + 1))
        cache[(i, j)] = result
        return result

    return get_max(0, 0)

def in_equilateral_triangle(height, i, j):
    return i >= 0 and i < height and j >= 0 and j < height

# Understanding:
#   f(i, j) = arr[i, j] +  max( f(i+1, j), f(i+1, j+1) )
#   e.g. [[1], [2, 3], [4,2,6], [4,6,8,2]]
#   The max of two (The max of two of points plus the parent) plus the parent
# Plan:
#   Iterate through the next to last row
#   Stamp out the value with the previous value plus it's direct two children
#   Continue to next row up, etc
#   return arr[0][0]
def triangle_bottom_up(arr):
    height = len(arr)

    for i in reversed(range(0, height - 1)):
        for j in reversed(range(0, i + 1)):
            arr[i][j] = arr[i][j] + max(arr[i + 1][j + 1], arr[i + 1][j])

    return arr[0][0]