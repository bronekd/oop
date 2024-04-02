from fraction import Fraction

f1 = Fraction(1,3)

print(f1)

f2 = Fraction(1,3)

print(f1 == f2)

f3 = f1 + f2
print(f3)

f3 += f2 # toto je __iadd__
print(f3)

f3 += 3 # toto je __iadd__
print(f3)