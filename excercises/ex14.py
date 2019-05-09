from sys import argv

script, user_name = argv
prompt = '?_?'

print("Hi %s, I'm the %s script." % (user_name, script))
print("I'd lile to ask you a few questions.")
print("Do you like me %s?" % user_name)
likes = input(prompt)

print("Where do you live %s?" % user_name)
lives = input(prompt)

print("What kind of computer do you have?")
computer = input(prompt)

print("Where do you go to school?")
school = input(prompt)

# % this is the format activator (to combine a """ style multiline string)
print("""
Alright, so you said %r about liking me.
You live in %r at %r. Not sure where that is.
And you have a %r computer. Nice.
""" % (likes, lives, school, computer))

# STUDY DRILLS
# 1 Zork and Adventure (see zork.py)
