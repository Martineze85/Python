import random

a = random.randint(1,7)
b = random.randint(1,7)
c = a + b

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
    print("El primer dado dio un valor de:", a)
    print("El segundo dado dio un valor de:", b)
    print("La suma da:", c)
else:
    print() 
