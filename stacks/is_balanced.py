def are_parentheses_balanced(parentheses):
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

print(are_parentheses_balanced('(())(()())'))
print(are_parentheses_balanced('(()('))

SUPPORTED_NOTATION = {
  '(': ')',
  '{': '}',
  '[': ']'
}

# Maintain a single stack
# Push opening characters onto stack
# For every closing closing character encountered that matches peek, pop
#   else, return false
# return whether stack is empty
def is_balanced(dictionaryOfPairs, subject):
  stack = []
  for char in subject:
    if char in dictionaryOfPairs.keys():
      stack.append(char)
      continue
    try:
      popped = stack.pop()
    except IndexError: # too many closing symbols
      return False
    if dictionaryOfPairs[popped] is not char: # mismatch
      return False

  return len(stack) == 0

print(is_balanced(SUPPORTED_NOTATION, '{[[]]}{[]}()'))
print(is_balanced(SUPPORTED_NOTATION, '{{{]]]['))