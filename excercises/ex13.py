# script is the same as .py file
# you import modules (ex. argv is a module or libary)
from sys import argv

# argv is argument variable
script, first, second, third = argv

print("The script is called:", script)
print("Your first variable is:", first)
print("Your second variable is:", second)
print("Your third variable is:", third)

#STUDY DRILLS
#1 ValueError: not enough values to unpack (expected 4, got 3)

#3 combine argv with input()
script, first_name, last_name = argv
middle_name = input("What's your middle name?")
print("Your full name is %s %s %s." % (first_name, middle_name, last_name))
