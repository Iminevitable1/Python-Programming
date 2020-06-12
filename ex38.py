ten_things = "Apples Oranges Crows Telephone Light Sugar"

print("Wait, there are not ten things in the list. Let's fix that.")

stuff = ten_things.split(' ')
more_stuff = ["Day", "Night", "Song", "Frisbee",
              "Corn", "Banana", "Girl", "Boy"]

while len(stuff) != 10:
    next_one = more_stuff.pop()
    print("Adding :", next_one)
    stuff.append(next_one)
    print(f"There are {len(stuff)} items now.")

print("There we go : ", stuff)

print("Let's do some things with stuff.")

print(stuff[1])
print(stuff[-5])# Whoa! Fancy.
print(stuff.pop())
print(', '.join(stuff))# What? Cool.
print(' #'.join(stuff[5:7]))# Super stellar!
