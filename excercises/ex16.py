from sys import argv

script, filename = argv

print("We're going to erase %r." % filename)
print("If you don't want that, hit CTRL-C (^C).")
print("If you do want that, hit RETURN.")

input("?")

print("Opening the file...")
# open the file in write mode
# + modifier changes the file modes: this will open the file in both read and
# write mode, depending on the character used, default for open is read ('r')
target = open(filename, 'w')

print("Truncating the file. Goodbye!")
# This is unnecessary since opening 'w' will overwrite the file, and truncates
# removes all data
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

target.write("%s\n%s\n%s\n" % (line1, line2, line3))
# target.write("\n")
# target.write(line2)
# target.write("\n")
# target.write(line3)
# target.write("\n")

print("And finally, we close it.")
target.close()

#STUDY DRILLS
#2 read the file you just created
#from sys import argv
#script, filename = argv

print("The %s file reads: " % filename)
read_target = open(filename)
contents = target.read
print(contents)
read_target.close()
