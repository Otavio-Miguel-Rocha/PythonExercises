import math
import cmath
a = float(input("A: "))
b = float(input("B: "))
c = float(input("C: "))

if a == 0:
    print("It's not Bhaskara equation")
else:
    delta = b**2-4*a*c
    if delta == 0:
        print("Just one root: ")
    elif delta > 0:
        print("Delta ", delta)
        print("X' ", (-b+cmath.sqrt(delta))/(a*2))
        print("X'' ", (-b-cmath.sqrt(delta))/(a*2))
    else:
        print("Irracional number")