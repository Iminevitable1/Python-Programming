print("Let's practice everything.")
print("You\'d need to know \'bout escapes with \\ that do:")
print("\n newlines and \t tabs")

poem = """
\t The lovely world
with logic so firmly planted
cannot discern \n the needs of love
nor comprehend passion from intuition
and requires an explanation
\n\t\twhere there is none.
"""

print("...................")
print(poem)
print("...................")
five = 10 - 2 + 3 - 6
print(f"This should be five : {five}")

def secret_formula(started):
    beans = started * 500
    jars = beans / 1000
    crates = beans / 100
    return beans, jars, crates

started = 10000
beans, jars, crates = secret_formula(started)

#Remember that this is another way of formatting a string
print("With a starting point of : {}".format(started))

#It's just like an f"" string
print(f"We'd have {beans} beans, {jars} jars, and {crates} crates.")

started = started / 10

print("We can also do that this way :")
formula = secret_formula(started)
#This is an easy way to apply a list to a format string
print("We'd have {} beans, {} jars, {} crates".format(*formula))
