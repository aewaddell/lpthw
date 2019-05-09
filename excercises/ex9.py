days = "Mon True Wed Thu Fri Sat Sun"
# (\n) is the newline command
# newline won't work when you use %r, because thats raw formatting (debugging)
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print("Here are the days: ", days)
print("Here are the months: ", months)

print """
There something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
"""
