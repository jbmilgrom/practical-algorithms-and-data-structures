from stack import Stack

def reverse_list(arr):
  stack = Stack()
  reversed = []
  for item in arr:
    stack.push(item)
  while stack.size() > 0:
    reversed.append(stack.pop())
  return reversed

print reverse_list([1,2,3,4])