# nové doplnění funkcí closures
#problematika scopes je v rámci paměti

def counter():
    number = 0
    def increment():
        nonlocal number #nonlocal sahám si do proměné mimo funkci. pokud bych to nedal uděla to novou proměnnou
        number += 1
        return number
    return increment




c = counter() # do ce vložím counter a je tam vložená celá vnořena funkce.
print(c())
print(c())


def print_Hello():
    print("Hello")
    return "return"

pozdrav = print_Hello() #funkce se závorkou se provede
pozdrav2 = print_Hello

print(pozdrav)
print(pozdrav2)

pozdrav2() #zavolám funkci
print_Hello()