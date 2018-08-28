# Understanding
#   f(k) = max(f(k-2) + arr[k], f(k-1))
def house_robber(arr):
    a, b = arr[0], arr[1]

    for i in range(2, len(arr)):
        a, b = b, max(a + arr[i], b)

    return b

print("testing")

assert house_robber([3, 2, 1, 5, 7]) == 11
assert house_robber([3, 10, 1, 5, 7, 3]) == 18

