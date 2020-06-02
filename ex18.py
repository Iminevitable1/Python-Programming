#This one is like your scripts with argv..
def print_2(*args):
    arg1, arg2 = args
    print(f"arg1: {arg1}, arg2: {arg2}")

#That args* is actually pointless, so we can just do this..
def print_2_agin(arg1, arg2):
    print(f"arg1: {arg1}, arg2: {arg2}")

#This just take one argument..
def print_1(arg1):
    print(f"arg1: {arg1}")

#This one takes no argument..
def print_none():
    print("I have no arguments.")

print_2("Hello", "World!")
print_2_agin("Hello", "again.")
print_1("Goodbye.")
print_none()
