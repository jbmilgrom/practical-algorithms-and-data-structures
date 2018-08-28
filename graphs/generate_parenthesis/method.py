from stacks.stack import Stack

OPEN = '('
CLOSE = ')'

# Understanding:
#   Valid: (())()
#   Invalid: )(()()
#   Valid: every parenthsis to the left is matched with one to the right
#   Generating combination:
#       [)*, (] -> [(), ((] -> [()(, ())*, (((, (()]
#   Counting:
#       n!/((n / 2)! + (n / 2)!) minus invalid states
# Problem:
#   Given a number n, return an array of strings,
#       each string representing a valid combination of n sets of parenthesis
# Plan:
#   Graph:
#       ['(' or ')'] -> ['(' or ')']
#   Generate the graph of all possible combinations
#       Maintain a stack of ( and of )
#       Bulid tree from popping from each stack
#       Perform a depth first search to reach valid paranthetical expressions
#           invalidate impossible paths
#               push thing back onto stack if invalid
#           when n*2 in length is reach, push into results
#           Each node should receive its own string
#   Maintain a results array

def generate_parenthesis(n):
    results, open, close = [], Stack(), Stack()

    for i in range(0, n * 2):
        open.push(OPEN) if i % 2 else close.push(CLOSE)

    def generate(expr):
        if len(expr) and cannot_be_valid(expr):
            return

        if open.is_empty() and close.is_empty():
            results.append(expr)
            return

        if not open.is_empty():
            open.pop()
            generate(expr + OPEN)
            open.push(OPEN)

        if not close.is_empty():
            close.pop()
            generate(expr + CLOSE)
            close.push(CLOSE)

    generate('')

    return results


# We want an invalidity chech that can be applied before a paranethetical expression is fully baked
# to avoid going down a bad path. That is what this attempts to solve.
#
# Understanding:
#   A balanced parenthetical expression has no closing tag without a corresponding opening
# Problem:
#   Identify a closing paren towards on the right that has no match on the left
# Plan:
#   Iterate from right to left
#       Push closing paren onto a stack
#       Pop stack when open paren is reached
#       return stack == empty
def cannot_be_valid(expr):
    close = Stack()

    for char in reversed(expr):
        if char == CLOSE:
            close.push(char)
            continue

        try:
            close.pop()
        # an opening paren was reached with no closing tags to the right of it, this _could_ be valid
        except IndexError:
            return False

    return not close.is_empty()



