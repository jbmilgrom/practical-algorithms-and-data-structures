import operator

ops = {'+': operator.add, '-': operator.sub}

def evaluate(expr):
    # Evaluates a sub-expression starting at index i.  There are two cases:
    #
    #     (1) i == 0, so we evaluate all of expr
    #     (2) i > 0 and expr[i - 1] == '(', so we evaluate until the matching ')'
    #
    # The return value is (result, j) where j is either len(expr) in case (1),
    # or the index after the closing ')' in case (2).
    def eval_rec(i):
        # For convenience, we pretend every expression starts with "0+" (which
        # doesn't change the result).
        result, op = 0, operator.add
        j = i
        while j < len(expr):
            c = expr[j]
            if c == '(':
                # Make a recursive call to handle the parenthesized
                # sub-expression.  Calling pushes a stack frame onto the
                # function call stack; this push is analogous to the other
                # solution pushing a '(' onto the state stack.
                value, j = eval_rec(j + 1)
                result = op(result, value)
            elif c == ')':
                # We can return here because we've finished processing the
                # parenthesized sub-expression.  Returning pops a stack frame off of
                # the function call stack; this pop is analogous to the other
                # solution popping until we've taken the opening '(' off of the
                # state stack.
                return result, j + 1
            elif c.isdigit():
                # If we see a digit, we can just apply the operator.  Since we
                # pretended that every expression starts with "0+", we won't
                # need to worry about the case where the digit we just saw was
                # the first operand for an operator.
                result = op(result, int(c))
                j += 1
            elif c in ops:
                # If we see an operator, we just keep track of it so that the
                # next time we see a value (either a digit or the result of a
                # parenthesized sub-expression), we can apply the operator we
                # just saw.
                op = ops[c]
                j += 1
            elif c.isspace():
                # Ignore blank characters.
                j += 1
            else:
                raise Exception("Unsupported symbol " + c)
        return result, j

    value, j = eval_rec(0)

    # We should have evaluated the entire input expression.
    assert j == len(expr)

    return value