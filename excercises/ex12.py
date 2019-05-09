age = input("How old are you?")
height = input("How tall are you?")
weight = input("How much do you weigh?")

print("So you're %s old, %s tall and %s heavy." % (
    age, height, weight))

# pydoc INPUT
# input([prompt]) -> value
# equivalent to eval(raw_input(prompt))
# pydoc module automatically generates documentation from Python modiles (help)

# pydoc OPEN
# open(name, [, mode[, buffering]]) -> file object
# Open a file using the file() type, returns a file object. This is the preferred
# way to open a file.

# pydoc file
# class file(object)
# file(name[, mode[, buffering]]) -> file object
# Open a file
# mode can be r (read), w (write) or a (append).
# A new file will be created for w or a if one does not already exist
# add a b for binary files
# add a + for simultaneous reading/writing
# add U to open file for input with universal newline
# Lots of Inner methods defined

# pydoc OS and SYS
