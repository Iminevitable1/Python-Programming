## Animal is-a object
class Animal(object):
    pass

## Dog is-a Animal
class Dog(Animal):

    def __init__(self, name):
        ## class dog has-a __init__ that takes self and name params
        self.name = named

## Cat is-a Animal
class Cat(Animal):

    def __init__(self, name):
        ## class Cat has-a __init__ that takes self and name as params
        self.name = name

## Person is-a Object
class Person(object):

    def __init__(self, name):
        ## class Person has-a __init__ that takes self and name as params
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## class Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## super() gives you access to methods in superclass from the subclass that inherits from it
        super(Employee, self).__init__(name)
        ## Employee has-a salary attribute
        self.salary = salary

## class Fish is-a Object
class Fish(object):
    pass

## class Salmon is-a Fish
class Salmon(Fish):
    pass

## class Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog .....OR..... Set rover to an instance of class Dog which has-a attribute Rover
rover = Dog("Rover")

## Set satan to an instance of class Cat which has-a attribute Satan
satan = Cat("Satan")

## Set mary to an instance of class Person which has-a attribute Mary
mary = Person("Mary")

## From mary, get the pet attribute  and set it to satan
mary.pet = satan

## frank is-a Employee which has-a attribute salary of 120000
frank = Employee("Frank", 120000)

## frank has-a pet attribute which is-a rover
frank.pet = rover

## Set flipper to an instance of class Fish
flipper = Fish()

## Set crouse to an instance of class Salmon
crouse = Salmon()

## Set harry to an instance of class Halibut
harry = Halibut()
