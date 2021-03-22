import random

dado = input("Quiere tirar los dados? (s)i o (n)o?")

while dado == "s":
    a = int(random.choice([1,2,3,4,5,6]))
    b = int(random.choice([1,2,3,4,5,6]))
    c = a + b
    print("Dale, tiremos los dados!")
    print("El primer dado dio un valor de:", a)
    print("El segundo dado dio un valor de:", b)
    print("La suma da:", c)
    dado = input("Quiere tirar los dados? (s)i o (n)o?")
