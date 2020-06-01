from sys import argv

script, name, aname = argv
symbol = ">> "

print(f"I would like to ask you a few questions {name}")
print(f"Which sports do you like the most {name} ? ")
sports = input(symbol)
#print(f"I like {sports} very much.")

print(f"Do you like painting ? ")
painting = input(symbol)
#print(f"I love to paint.")

print(f"""So from the above answers,
that you have given to me,
I can say that you like {sports}
and you love ot paint, don't you ?
{symbol}{painting}.""")

print(f"By the way, what sports do you like {aname} ?")
sports = input(symbol)

print(f"Are you also fond of painting like {name} ?")
painting = input(symbol)

print(f"""I can conclude that {aname} likes {sports}
and don't like to piant.
Isn't that right {aname} ?
{symbol}{painting} """)
