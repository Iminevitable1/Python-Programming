#USING A WHILE LOOP.......
#i = 0
#numbers = []
#j = int(input("j = "))

#while i < 20:
#     print(f"At the top i is {i}")
#     numbers.append(i)

#     i = i + j
#     print("Numbers now: ", numbers)
#     print(f"At the bottom i is {i}")

#print("The numbers: ")
#for num in numbers:
#    print(num)

#USING A FUNCTION......
numbers = []
i = int(input("i = "))
x = int(input("x = "))
j = int(input("j = "))
def func(i,x):
    if i < x:
        print(f"At the top i is {i}.")
        numbers.append(i)
        i = i + j
        print("Numbers now : ", numbers)
        print(f"At the bottom i is {i}.")
        func(i,x)
    return numbers

numbers = func(i,x)
for num in numbers:
    print(num)

#USING  A FOR LOOP......
#i = int(input("i = "))
#x = int(input("x = "))
#nos = []

#for i in range(i,x):
#    print(f"At the top is i is {i}")
#    nos.append(i)

#    for i in range(i,i+1):
#        print("Numbers now : ",nos)
#        print(f"At the bottom i is {i}")

#print("The numbers are:")
#for n in nos:
#    print(n)
