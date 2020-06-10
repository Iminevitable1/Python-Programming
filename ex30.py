people = 48
cars = 37
trucks = 50

if cars > people:
    print("We should take the cars.")

elif cars < people:
    print("We can't take the cars.")

else:
    print("We can't decide.")

if trucks > cars:
    print("That's too many trucks.")

elif trucks < cars:
    print("Maybe we could take the trucks.")

else:
    print("We still can't decide.")

if people > trucks:
    print("Alright ! Let's just take these trucks.")

else:
    print("Fine ! Let's stay home then.")

if cars < trucks or trucks > people == True:
    print("It's time to get going.")

if not(cars == trucks and people == cars) == True:
    print("It's complex but it's True.")
