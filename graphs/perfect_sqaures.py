from stacks.queue import Queue

'''
e.g.
13 = 9 + 4, so answer is 2
12 = 4 + 4 + 4, so answer is 3

Understanding:
  All numbers are comprised of at least n 1's
  n cannot be comprised of a perfect square larger than n

Plan:
  Brute force graph search:
    intialize root of graph equal to 0
    [1, 2, ... i * i < n]
            |
    [1, 2, ... i * i < n]
    ...
    Search for minimum depth that sums to n
      Depth first search
      Track levels with nodes
      When sum is found, return level
'''
def least_perfect_sqaures_that_sum_to(n):
  # generate sufficient range of squares
  squares = []
  for i in range(1, n + 1):
    squares.append(i * i)

  q = Queue()
  q.enqueue((0, 0)) # (level, sum)
  while not q.is_empty():
    level, sum = q.dequeue()
    if sum == n:
      return level
    for s in squares:
      q.enqueue((level + 1, sum + s))


