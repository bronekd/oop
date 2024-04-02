# toto je kod od učitele 
class City:
    def __init__(self, name, long, lat):
        self.name = name
        self.long = long
        self.lat = lat

    # magic metoda str volá co to bude dělat. napíšu co má dělat když volám c1
    def __str__(self):
        return (f"""Name: {self.name},
Long: {self.long}
Lat: {self.lat}""")


    # porovnávání
    def __eq__(self, other):
        return self.long == other.long and self.lat == other.lat

c1 = City("Prag", 20, 30)
c2 = City("Berlin", 20, 30)

print(c1) #Pěkný vypis pomocí str
print()
print(c1 == c2) # true dělá metoda __eq__


