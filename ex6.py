types_of_people = 2
x = f"There are {types_of_people} types of people."

mango = "mango"
do_not = "don't"

y = f"who likes {mango} and those who {do_not}."

print(x)
#In the following line the details in the print function joins with the above line.
print(f"Those {y}")

print("By the way, I love mangoes.")

hilarious = True

about_above = "I did say right. Didn't I ?  {}"

#.format() function is used to apply format on already crerated string.
print(about_above.format(hilarious))

a = "What I said above, "
b = "don't take it seriously..."

#The following line joins both of the above lines and then print them.Its called string cocatenation.
print(a+b)
