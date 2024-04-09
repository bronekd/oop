"""
f1 = Fraction(1,3)

print(f1)

f2 = Fraction(1,3)

print(f1 == f2)

f3 = f1 + f2
print(f3)

f3 += f2 # toto je __iadd__
print(f3)

try:
    f3 += 3 # toto je __iadd__
    print(f3)
except MyCustomError as e:
    print("Moje chyba zde testuje moje zprávy chyb")

"""

"""
#další úkol
#využití dědičnosti ale tak, že první je vehicle a pak to rozšiřuje car ale já přes import car využívám třídu vehicle.
from car import Car
c1 = Car("Skoda", "cerna")

print(c1.name)
c1.start()
"""

# od tadyma nefunguje výpošt tvarů 10
from fraction import Fraction
from my_error import MyCustomError
from car import Car
#from geometry import *
import geometry

# další úkol počítání plochy
#circle = Circle("Kruh", 5)
#print(f"Plocha {circle.name} je: {circle.calculate_area()}")


#squer = Circle("Kruh", 5)
#print(f"Plocha {circle.name} je: {circle.calculate_area()}")

# zde končí nefunguje 10





# ukol Animal







