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

#opraveny výpočet tvarů

from geometry import *
#circle = geometry.Circle("Kruh", 5)
circle = Circle("Kruh", 5)
print(f"Plocha {circle.name} je: {circle.calculate_area()}")

#square = Square("Ctverec", 4) # Nefunguje
#print(f"Plocha {square.name} je: {square.calculate_area()}")

rectangle = Rectangle("Obdelnik", 3, 6)
print(f"Plocha {rectangle.name} je: {rectangle.calculate_area()}")








