from graphs.file_system.method import longest_file_path


print('############################')
print('Testing File System String Parse')
print('############################')

# input = "dir1\n\tdir2\n\tdir3\n\t\tfile.txt\ns.txt"
# received = longest_file_path(input)
# assert received == 18, "Expected {}; received {}".format(18, received)

# input = "dir1\n\tdir2\n\t\tf.txt\n\tdir3\n\t\tfile.txt\ns.txt"
# received = longest_file_path(input)
# assert received == 18, "Expected {}; received {}".format(18, received)

input = "dir1\n\tdir2\n\tdir3\n\t\tfile.txt\nsuperlongfilenamemeow.txt"
received = longest_file_path(input)
expected = len('superlongfilenamemeow.txt')
assert received == expected, "Expected {}; received {}".format(expected, received)