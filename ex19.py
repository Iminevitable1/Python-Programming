def fruit(apple, banana):
    print(f"You have {apple} apples.")
    print(f"You also have {banana} bananas.")
    print("Man, that's enough for a week.")
    print("Now get some vegetables also.\n")

print("We can give the function numbers directly..")
fruit(16, 23)

print("Or, we can use variables from our script..")
number_of_apples = 7
number_of_bananas = 12
fruit(number_of_apples, number_of_bananas)

print("We can do even math inside..")
fruit(5+9, 2+7)

print("And we can also combine variables and math..")
fruit(number_of_apples + 26, number_of_bananas + 57)

print("We can do it by taking input fromt the user..")
#num_of_apples = input()
#num_of_bananas = input()
fruit(int(input()), int(input()))

#There are so many other ways of doing this program;
#For example : 1.Using command line arguments.
              #2.We can assign a new name to the function and call it by its new name.
              #3.We can also pass a function as an argument.
