tabby_cat = "I'm \"tabbed\" in"
persian_cat = "I'm a split \non a line."
backslash_cat = "I'm \\a cat\\ ."
fat_cat = '''I'll do a list :
*\tCat food.
*\tcan be only be
*\t\r\t\f\tpurchased from pet's food shop.
'''

print(tabby_cat)
print(backslash_cat)
print(persian_cat)
print(fat_cat)
print("\a")

ice = "{}"

print(ice.format("You shouldn't be here."))
print("You {} here.".format("\nshouldn't be"))

fire = "{} {}"

print("""
\t\f\t\fYou shouldn't
\f\t\f\tbe here.
""")
