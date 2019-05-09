from sys import argv
from os.path import exists

script, from_file, to_file = argv

# print("Copying from %s to %s" % (from_file, to_file))

# we could do these two on one line too, how?
# in_file = open(from_file)
# indata = in_file.read()

# len returns the length of the string
# print("The input file is %d bytes long" % len(indata))
# print("Does the output file exist? %r" % exists(to_file))
# print("Ready, hit RETURN to continue, CTRL-C to abort.")
# input()

# out_file = open(to_file, 'w')
# out_file.write(indata)

open(to_file, 'w').write(open(from_file).read())

# print("Alright, all done.")

# out_file.close()
# in_file.close()

# STUDY DRILLS
# import searches for the named module, then binds the results of that search
# to a name in local scope - then you gain access to the code in another module.

# cat function in terminal - concatenates files together - can be used to
# print a file to the screen.
