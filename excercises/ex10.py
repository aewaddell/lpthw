tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

# You can use triple single quote instead
fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print(tabby_cat)
print(persian_cat)
print(backslash_cat)
print(fat_cat)

# \\ : backslash
# \' : single-quote
# \" : double-quotes
# \a : ASCII bell
# \b : ASCII backspace
# \f : ASCII formfeed
# \n : ASCII linefeed (newline)
# \N{name} : character named name in Unicode database
# \r : ASCII carriage return
# \t : ASCII horizontal tab
# more...

# while True:
#     for i in ["/", "-", "|", "\\", "|"]:
#         print("%r\r" % i,)

#Assign string value for each variable
intro = "I'll print a week:"
mon = "Mon"
tue = "Tue"
wed = "Wed"
thu = "Thu"
fri = "Fri"
sat = "Sat"
sun = "Sun"

print("%s\n%s\t%s\t%s\t%s\t%s\t%s\t%s\n" % (intro, mon, tue, wed, thu, fri, sat, sun))

# %s uses the string function and %r uses the repr function
# %r prints what you'd write in your file (for debugging)
    # escape characters don't work in this mode
#but %s prints it the way you'd like to see it. (for displaying)
print("%r" % intro)
print("%r" % "She said \"I'll print a week\"")

print("%s" % intro)
print("%s" % "She said \"I'll print a week\"")
