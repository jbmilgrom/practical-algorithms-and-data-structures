from stack import Stack

OPERATIONS = {
  '+': lambda x, y: x + y,
  '-': lambda x, y: x - y
}

# 2 - (1 + 2) => -1
# 2 + 9 + 3 => 14
# alg:
#   1. Calculate string left to right
#     a. num:
#       i. if top of stack is op, eval (pop() x 2)
#       ii. if not, push unto stack
#     b. op: push onto stack
#     c. (: push onto stack
#     d. ): remove open parenthesis and eval num
#   
def calculate(string):
  def evaluate(stack, char):
    op = OPERATIONS[stack.pop()]
    num1 = stack.pop()
    return str(op(int(num1), int(char)))

  def handleDigit(stack, characterDigit):
    next = characterDigit
    if stack.size() > 0 and stack.peek() in OPERATIONS:
      next = evaluate(stack, next)
    stack.push(next)

  stack = Stack()
  for char in string:
    if char == ')':
      digit = stack.pop()
      stack.pop() # pop the open parenthesis
      handleDigit(stack, digit)
    if char.isdigit():
      handleDigit(stack, char)
    if char in OPERATIONS or char == '(':
      stack.push(char)
  return int(stack.pop())

print calculate("3 + 4")
print calculate("3 - 4")
print calculate("3 - (5 + 3)")
print calculate("3 - (5 + 3 - (2 + 3)) + 4")



