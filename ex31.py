print("""You enter a dark room with two doors.
Do you go through door #1 or door #2?""")

door = input("> ")

if door == "1":
    print("There's a giant bear here eating a cheesecake.")
    print("What do you do?")
    print("1. Take the cake.")
    print("2. Scream at the bear.")

    bear = input("> ")

    if bear == "1":
        print("The bear eats your face off. Good job!")
    elif bear == "2":
        print("The bear eats your legs off. Good job!")
    else:
        print(f"Well, doing {bear} is comparatively better.")
        print("Bear runs away.")

elif door == "2":
    print("You stare into endless abyss at Cthulhu's retina.")
    print("1. Blueberries.")
    print("2. Yellow jacket clothespins.")
    print("3. Understand revolvers yelling melodies.")

    insanity = input("> ")

    if insanity == "1" or insanity == "2":
        print("Your body survives powered by a mind of jello.")
        print("Good job!")
    else:
        print("The insanity rots your eyes in a pool of muck.")
        print("Good job!")
else:
    print("You stumble around and fall on a knife an die. Good job!")

print("--------------------------------------")
print("Here's a new game if you're bored.")
print("""There are two jars full of liquids.
These both liquids have powerfull abilities and you can only choose one.
Which one will you choose?""")

jar = input("> ")

if jar == "1":
    print("You would memorize anything by reading it 1 time only.")
    print("What would you memorize?")
    print("1. History")
    print("2. All of Mathematics equations.")
    print("3. Whole Chemistry.")

    memorize = input("> ")

    if memorize == "1":
        print("You would be a master of History.")
    elif memorize == "2":
        print("You would do math in seconds. Congrats!")
    elif memorize == "3":
        print("The Chemistry lab is all yours.")
    else:
        print("The power of the liquid will finish.")

elif jar == "2":
    print("You will get to choose from the following.")
    print("What will you choose?")
    print("1. A house with all facilities.")
    print("2. Any vehicle you want.")

    choose = input("> ")

    if choose == "1":
        print("Now you won't have to purchase anything. Good job!")
    elif choose == "2":
        print("You can buy any vehicle and go to any place you want.")
    else:
        print("Nothing other than this. Sorry!")

else:
    print("That's it. You won't get any other liquids.")
