# Understanding
#   f(k) = max(f(k-2) + arr[k], f(k-1))
def house_robber(arr):
    a, b = arr[0], arr[1]

    for i in range(2, len(arr)):
        a, b = b, max(a + arr[i], b)

    return b


# Understanding
#   Now, house can also rob i.e. negative numbers
#   So, now, f(k) = max(max(f(k-2), f(k-2) + arr[k]), f(k-1))
def robber_robber(arr):
    a, b = max(0, arr[0]), max(0, arr[1])

    for i in range(2, len(arr)):
        a, b = b, max(max(a, a + arr[i]), b)

    return b
