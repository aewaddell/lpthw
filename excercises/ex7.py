print("Mary had a little lamb.")
# snow is not a variable it is a string with the word 'snow' in it. 
print("Its fleece was white as {}.".format('snow'))
print("And everywhere that Mary went.")
print("." * 10) # this will print a . 10 times

end1 = "C"
end2 = "h"
end3 = "e"
end4 = "e"
end5 = "s"
end6 = "e"
end7 = "B"
end8 = "u"
end9 = "r"
end10 = "g"
end11 = "e"
end12 = "r"

# watch end = '' at the end. Try removing it and see what happens
# It adds a space between the two words (ends the string with a space)
print(end1 + end2 + end3 + end4 + end5 + end6, end = ' ')
print(end7 + end8 + end9 + end10 + end11 + end12)

#BREAK IT
# (end1 * end2) can't multiply sequence by non-int of type 'str'
# (end12 = 9) can only concatenate str, not int
