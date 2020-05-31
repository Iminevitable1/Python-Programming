formatter = "{} {} {} {} {}"

print(formatter.format('Please', 'turn', 'at', 'this', 'point'))
print(formatter.format(5+5,2+3,5-4,2-9,8))
print(formatter.format(formatter,formatter,formatter,formatter,formatter,formatter))
print(formatter.format(True,False,True,True,False))
print(formatter.format(
        "You should",
        "write",
        "something here.",
        "Nothing in here is",
        "worthful to write."
))
