from stack import Stack

OPERATIONS = {
  '+': lambda x, y: x + y,
  '-': lambda x, y: x - y
}

# 2 - (1 + 2) => -1
# 2 + 9 + 3 => 14
# alg:
#   1. iterate string left to right
#     a. num:
#       i. if top of stack is op, eval (pop() x 2)
#       ii. if not, push unto stack
#     b. op: push onto stack
#     c. (: push onto stack
#     d. ): remove open parenthesis and eval num
#   
def evaluate(string):
  stack = Stack() # Stack<string>
  for char in string:
    if char in OPERATIONS or char == '(':
      stack.push(char)
    if char == ')':
      digit = stack.pop()
      stack.pop() # pop the open parenthesis
      handleDigit(stack, digit)
    if char.isdigit():
      handleDigit(stack, char)

    # ignore other characters

  return int(stack.pop())

# @private
def handleDigit(stack, digit):
  next = digit
  if stack.size() > 0 and stack.peek() in OPERATIONS:
    next = call(stack.pop(), stack.pop(), digit)
  stack.push(next)

# @private
def call(op, leftDigit, rightDigit):
  return str(OPERATIONS[op](int(leftDigit), int(rightDigit)))

# TEST
print evaluate("3 + 4")
print evaluate("3 - 4")
print evaluate("3 - (5 + 3)")
print evaluate("3 - (5 + 3 - (2 + 3)) + 4")