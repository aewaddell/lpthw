# f-string or .format() - formats variables in strings
# f"some stuff here {avariable}"
# f"some other stuff {anothervar}"

# Sets a variable name (int)
types_of_people = 10
# Sets a variable name to an f-string
x = f"There are {types_of_people}."

binary = "binary"
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

# print the two variables
print(x)
print(y)

# print the two variables inside further f-strings (these are nested f-strings)
print(f"I also said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

# Using the .format method instead of f-string
print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side"

# You can concatenate strings
print(w + e)

#STUDY DRILLS
#2 a string is put inside another string 4 times
#BREAK IT AND FIX IT
