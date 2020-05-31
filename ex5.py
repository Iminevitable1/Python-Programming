name = 'Jake'
age =  19
height = 165
weight = 70
eyes = 'Black'
teeth = 'White'
hair = 'Black'


print(f"Let's talk about {name}")
print(f"He is {height} cms tall.")
print(f"He is {weight} kgs. heavy.")
print("That's not quite heavy.")
print(f"He has {teeth} teeth.")
print(f"He has {hair} hair.")
print("Not a single white hair till date.")

#The followig equation is somewhat tricky, so make sure you understand it clearly.
total = height - ( weight + age )
print(f"If I add {weight} and {age} and then subtract it from {height}, I would get {total}.")

pound = 1
kg = 0.453592
cm = 2.54
inch = 1

sum = ( inch * height ) / cm
total = ( weight * pound ) / kg
print(f"I'm {total} pounds heavy.")
print(f"I'm {sum} inches tall.")
