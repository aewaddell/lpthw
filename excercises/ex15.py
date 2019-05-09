from sys import argv

script, filename = argv

# open the file and assign it a variable name (makes a file object)
txt = open(filename)

print("Here's your file %r:" % filename)
# read the open file
print(txt.read())

txt.close()

print("Type the filename again:")
#file_again = input("> ")
file_again = filename

#open the file again from inputted variable name instead of argument
txt_again = open(file_again)

print(txt_again.read())

txt_again.close()
# STUDY DRILLS
# commands are also called functions or methods

#pydoc FILE READ()
# read([size]) -> read at most size bytes, returned as a string.
# if the size argument is negative or omitted, read until EOF is reached.
# Notice that when in non-blocking mode, less data than what was requested may
# returned, even if no sie parameter was given.
