cars = 100.0
space_in_a_car = 5.0
drivers = 50.0
passengers = 100.0
cars_not_driven = cars - drivers
cars_driven = drivers
average_passengers_per_car = passengers / cars_driven
car_capacity = cars_driven*space_in_a_car

print("There are", cars ,"avilaible at this time.")
print("But the number of drivers available at this time are only", drivers ,".")
print("So there will be", cars_not_driven ,"empty cars.")
print("We can transport", car_capacity ,"passengers today.")
print("We have", passengers ,"passengers to transport today.")
print("In each car there will be only", average_passengers_per_car ,"passengers.")
