from fraction import Fraction
from my_error import MyCustomError

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


#další úkol
from car import Car
c1 = Car("Skoda", "cerna")

print(c1.name)
c1.start()
