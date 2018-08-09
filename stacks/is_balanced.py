def is_balanced(parentheses):
  stack = []
  OPENING = '('
  for char in parentheses:
    if char == OPENING:
      stack.append(char)
    else:
      try:
        stack.pop()
      except IndexError:
        return False
  return len(stack) == 0

print is_balanced('(())(()())')
print is_balanced('(()(')