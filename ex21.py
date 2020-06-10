def add(a,b):
    print(f"Adding {a} and {b}.")
    return a + b

def sub(a,b):
    print(f"Subtracting {b} from {a}.")
    return a - b

def mul(a,b):
    print(f"Multiplying {a} and {b}.")
    return a * b

def div(a,b):
    print(f"Dividing {b} from {a}.")
    return a / b

print("Let's do some math with just functions.")

age = add(19,5)
height = sub(190,25)
weight = mul(35,2)
iq = div(150,2)

print(f" Age : {age}\n Height : {height}\n Weight : {weight}\n IQ : {iq}")

print("Here's a puzzle for you...")

#how =  add(age, sub(height, mul(weight, div(iq,2))))
how = div(iq,2)
what = mul(weight,how)
which = sub(height, what)
when = add(age, which)

print(f"The answer of the above puzzle is {when}; Can you do it manually ?")

print("What is the answer of this puzzle : 24 + 35 / 5 - 64 / 4 * 16 + 300 - 100 + 31 - 59")

hey = sub(add(sub(add(sub(add(24,div(35,5)),div(64,mul(4,16))),300),100),31),59)

print(f"So, the answer of the above puzzle is {hey}.")
