def sumIterativeLoop(n):
  sum = 0
  for i in range(n + 1):
    sum += i
  return sum

print("sumIterativeLoop(3)")
print(sumIterativeLoop(3))

def sumIterativeRecursive(n):
  def iterate(n, sum):
    if n == 0:
      return sum
    return iterate(n - 1, sum + n)
  return iterate(n, 0)

print("sumIterativeRecursive(3)")
print(sumIterativeRecursive(3))

def sumRecursive(n):
  if n == 0:
    return n
  return n + sumRecursive(n - 1)

print("sumRecursive(3)")
print(sumRecursive(3))

# n == 3; 3/2 => 1.5 * 4 => 6
# n == 4: 4/2 => 2 * 5 => 10
def sumNConstantTime(n):
  return (n+1) * n//2

template = '{}({}): {:5d}'
for i in range(1, 10):
  print(template.format('sumNConstantTime', i, sumNConstantTime(i)))

