def sumIterativeLoop(n):
  sum = 0
  for i in range(n + 1):
    sum = sum + i
  return sum

print "sumIterativeLoop(3)"
print sumIterativeLoop(3)

def sumIterativeRecursive(n):
  def iterate(n, sum):
    if(n == 0):
      return sum
    return iterate(n - 1, sum + n)
  return iterate(n, 0)

print "sumIterativeRecursive(3)"
print sumIterativeRecursive(3)

def sumRecursive(n):
  if (n == 0):
    return n
  return n + sumRecursive(n -1)

print "sumRecursive(3)"
print sumRecursive(3)