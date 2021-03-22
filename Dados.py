import random

a = random.randint(1,6)
b = random.randint(1,6)
c = a + b

d = random.randint(1,6)
e = random.randint(1,6)
f = d + e


dado = input("Quiere tirar los dados? (s)i o (n)o?")

if dado == "s":
    print("Dale, tiremos los dados!")
    print("El primer dado dio un valor de:", a)
    print("El segundo dado dio un valor de:", b)
    print("La suma da:", c)
else:
    print() 

dado = input("Quiere tirar los dados? (s)i o (n)o?")

if dado == "s":
    print("Dale, tiremos los dados!")
    print("El primer dado dio un valor de:", d)
    print("El segundo dado dio un valor de:", e)
    print("La suma da:", f)
else:
    print() 
