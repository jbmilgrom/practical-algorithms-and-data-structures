# Given a string like "dir1\n\tdir2\n\tdir3\n\t\tfile.txt\ns.txt"
# which corresponds to:
#   dir1
#       dir2
#       dir3
#           file.txt
#   s.txt
#
# Return the length of the largest path by character count
# In this case,
#   'dir1/dir3/file.txt' => 18
#
# Note that files are identifiable by the '.' character

# Understanding:
#   \n chararacters ends a word
#   \t determine the level of the next file or directory
#   . indicates a file
#
#   after a new line, \t's determine where the next word should go
#
# Plan:
#   Maintain a Stack<total>
#       pop when \t's are less
#       push when \t's are more
#       build word when char

TAB = '\t'
NEW_LINE = '\n'
FILE_CHAR = '.'

def longest_file_path(input):
    stack, max_length, prev = [], 0, None
    word, is_directory, dir_level = '', True, 0

    for char in input + NEW_LINE:
        if char is not TAB and char is not NEW_LINE:
            word = word + char

            # we know that we now can determine the level of the upcoming word
            if prev == NEW_LINE:

                # 0 is valid level; we need to offset by one
                while dir_level <= len(stack) - 1:
                    stack.pop()

        if char is FILE_CHAR:
            is_directory = False

        if char is NEW_LINE:
            try:
                total = stack[-1]
            except IndexError:
                total = 0

            total = total + len(word)

            if not is_directory: # is file
                max_length = max(max_length, total)
            else:
                stack.append(total + 1)

            word, is_directory, dir_level = '', True, 0

        if char is TAB:
            dir_level += 1

        prev = char

    return max_length

# Understanding:
#   break string into prefixed words
#   if depth is greater than current depth:
#       push onto stack
#   else:
#       pop from stack
#   if word is file, check with max and continue
def longest_file_path_graph(input):
    words_prefixed_with_depth = input.split('\n')
    stack, longest, previous_level = [], 0, 0

    for word in words_prefixed_with_depth:
        dir_level, is_directory = 0, True

        for char in word:
            if char is FILE_CHAR:
                is_directory = False

            if char is TAB:
                dir_level+=1

        try:
            total = stack[-1]
        except IndexError:
            total = 0

        next_total = total + len(word)

        if not is_directory:
            longest = max(longest, next_total)

        elif dir_level > previous_level:
            stack.append(next_total)

        else:
            # 0 is valid level; we need to offset by one
            while dir_level <= len(stack) - 1:
                stack.pop()

        previous_level = dir_level

    return longest




